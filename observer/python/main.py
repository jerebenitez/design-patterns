from stock import Stock
from investor import Investor
import time
from typing import List
from threading import Thread
import logging


def test_apple_stock(investors: List[Investor]):
    stock = Stock("Apple", "$AAPL", 131.00, 0.25, 0.35, 1.0/252.0, 252*5)

    for investor in investors:
        stock.attach(investor)

    for i in range(252*2):
        time.sleep(0.5)
        stock.step()

    for investor in investors:
        stock.detach(investor)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    goldman = Investor("Goldman Sachs")

    proc1 = Thread(target=test_apple_stock, args=([goldman], ))

    proc1.start()
