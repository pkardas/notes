import json
from typing import Dict

from redis.client import Redis
from sqlmodel import create_engine

from src import config
from src.adapters.orm import create_db_and_tables
from src.domain import (
    commands,
    events,
)
from src.service_layer import message_bus
from src.service_layer.unit_of_work import UnitOfWork

r = Redis(**config.get_redis_host_and_port())


def main():
    engine = create_engine(config.get_postgres_uri())
    create_db_and_tables(engine)

    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("change_batch_quantity")

    for m in pubsub.listen():
        handle_change_batch_quantity(m)


def handle_change_batch_quantity(message: Dict):
    event = events.BatchQuantityChanged(**json.loads(message["data"]))
    cmd = commands.ChangeBatchQuantity(ref=event.batch_ref, qty=event.qty)

    message_bus.handle(message=cmd, uow=UnitOfWork())


if __name__ == "__main__":
    main()
