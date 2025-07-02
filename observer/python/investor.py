from pubsub import Subscriber
import logging


class Investor(Subscriber):
    _stocks = {}

    def __init__(self, name: str):
        self.name = name

    def update(self, ticker, price) -> None:
        if ticker not in self._stocks:
            self._stocks[ticker] = price
            logging.info(f"{ticker} stock indexed for the first time")
        else:
            if self._stocks[ticker] > price:
                logging.info(f"{ticker} stock price went down!")
            elif self._stocks[ticker] < price:
                logging.info(f"{ticker} stock price went up!")

            self._stocks[ticker] = price
