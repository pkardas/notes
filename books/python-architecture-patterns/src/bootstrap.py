import inspect
from typing import Callable

from sqlalchemy.engine import Engine
from sqlmodel import create_engine

from src import config
from src.adapters import redis_publisher
from src.adapters.notifications import (
    AbstractNotifications,
    EmailNotifications,
)
from src.adapters.orm import create_db_and_tables
from src.service_layer.message_bus import (
    COMMAND_HANDLERS,
    EVENT_HANDLERS,
    MessageBus,
)
from src.service_layer.unit_of_work import (
    AbstractUnitOfWork,
    UnitOfWork,
)


def bootstrap(start_orm: bool = True, engine: Engine = create_engine(config.get_postgres_uri()), uow: AbstractUnitOfWork = UnitOfWork(),
              notifications: AbstractNotifications = EmailNotifications(), publish: Callable = redis_publisher.publish):
    if start_orm:
        create_db_and_tables(engine)

    dependencies = {"uow": uow, "notifications": notifications, "publish": publish}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in COMMAND_HANDLERS.items()
    }

    return MessageBus(uow=uow, event_handlers=injected_event_handlers, command_handlers=injected_command_handlers)


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)
