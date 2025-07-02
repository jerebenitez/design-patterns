import numpy as np
import logging
from typing import List
from pubsub import Publisher, Subscriber


class Stock(Publisher):
    """
    source: https://www.pyquantnews.com/the-pyquant-newsletter/how-to-simulate-stock-prices-with-python
    """
    _subscribers: List[Subscriber] = []

    def __init__(self, name: str, ticker: str,
                 initial_price: float, volatility: float, drift: float,
                 delta: float, time: int):

        if 1 < volatility < 0 or 1 < drift < 0:
            raise ValueError("Invalid values for stock.")

        self.name = name
        self.ticker = ticker
        self.t = -1

        process = volatility * np.random.normal(
                loc=0,
                scale=np.sqrt(delta),
                size=(time, 1))
        gbm = np.exp(process + (drift - volatility**2 / 2) * delta)
        stacked = np.vstack([np.ones(1), gbm])

        self.prices = initial_price * stacked.cumprod(axis=0)

    def attach(self, observer: Subscriber) -> None:
        self._subscribers.append(observer)
        logging.info(f"{observer.name} subscribed to {self.name}")

    def detach(self, observer: Subscriber) -> None:
        self._subscribers.remove(observer)
        logging.info(f"{observer.name} unsubscribed to {self.name}")

    def notify(self):
        for observer in self._subscribers:
            observer.update(self.ticker, self.prices[self.t])

    def step(self):
        self.t += 1
        self.notify()
