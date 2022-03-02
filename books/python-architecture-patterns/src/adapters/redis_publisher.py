from redis.client import Redis

from src import config
from src.domain.events import Event

r = Redis(**config.get_redis_host_and_port())


def publish(channel: str, event: Event):
    r.publish(channel, event.json())
