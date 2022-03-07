import logging
from typing import (
    Callable,
    Dict,
    List,
    Type,
    Union,
)

from src.domain import (
    commands,
    events,
)
from src.service_layer import handlers
from src.service_layer.unit_of_work import AbstractUnitOfWork

logger = logging.getLogger(__name__)

Message = Union[commands.Command, events.Event]

EVENT_HANDLERS: Dict[Type[events.Event], List[Callable]] = {
    events.OutOfStock: [handlers.send_out_of_stock_notification],
    events.Allocated: [handlers.publish_allocated_event, handlers.add_allocation_to_read_model],
    events.Deallocated: [handlers.remove_allocation_from_read_model, handlers.reallocate]
}

COMMAND_HANDLERS: Dict[Type[commands.Command], Callable] = {
    commands.CreateBatch: handlers.add_batch,
    commands.ChangeBatchQuantity: handlers.change_batch_quantity,
    commands.Allocate: handlers.allocate,
}


class MessageBus:
    def __init__(self, uow: AbstractUnitOfWork, event_handlers: Dict[Type[events.Event], List[Callable]], command_handlers: Dict[Type[commands.Command], Callable]):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

        self.queue: List[Message] = []

    def handle(self, message: Message):
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
                self._handle_event(message)
            elif isinstance(message, commands.Command):
                self._handle_command(message)
            else:
                raise Exception(f"{message} was not an Event or Command")

    def _handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug(f"Handling event {event} with handler {handler}")
                handler(event)
                self.queue.extend(self.uow.collect_new_messages())
            except Exception as e:
                logger.exception(f"Exception handling event {event}: {e}")
                continue

    def _handle_command(self, command: commands.Command):
        try:
            handler = self.command_handlers[type(command)]
            handler(command)
            self.queue.extend(self.uow.collect_new_messages())
        except Exception:
            logger.exception("Exception handling command %s", command)
            raise
