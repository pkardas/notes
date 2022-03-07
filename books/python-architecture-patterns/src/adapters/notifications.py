from abc import (
    ABC,
    abstractmethod,
)
import smtplib

from src import config

DEFAULT_HOST = config.get_email_host_and_port()["host"]
DEFAULT_PORT = config.get_email_host_and_port()["port"]


class AbstractNotifications(ABC):
    @abstractmethod
    def send(self, destination, message):
        raise NotImplementedError


class EmailNotifications(AbstractNotifications):
    def __init__(self, smtp_host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.server = smtplib.SMTP(smtp_host, port=port)
        self.server.noop()

    def send(self, destination, message):
        self.server.sendmail(
            from_addr="allocations@example.com",
            to_addrs=[destination],
            msg=f"Subject: allocation service notification\n{message}",
        )
