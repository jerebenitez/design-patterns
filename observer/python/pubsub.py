from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, ticker: str, price: float) -> None:
        pass


class Publisher(ABC):
    @abstractmethod
    def attach(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def detach(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
