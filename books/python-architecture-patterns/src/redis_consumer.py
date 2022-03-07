import json
from typing import Dict

from redis.client import Redis

from src import config
from src.bootstrap import bootstrap
from src.domain import (
    commands,
    events,
)
from src.service_layer.message_bus import MessageBus

r = Redis(**config.get_redis_host_and_port())


def main():
    bus = bootstrap()
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("change_batch_quantity")

    for m in pubsub.listen():
        _handle_change_batch_quantity(m, bus)


def _handle_change_batch_quantity(message: Dict, bus: MessageBus):
    event = events.BatchQuantityChanged(**json.loads(message["data"]))
    cmd = commands.ChangeBatchQuantity(ref=event.batch_ref, qty=event.qty)

    bus.handle(message=cmd)


if __name__ == "__main__":
    main()
