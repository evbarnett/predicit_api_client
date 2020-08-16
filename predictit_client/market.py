from .contract import Contract
from typing import *


class Market:
    """

    MIT, github.com/evbarnett
    """

    def __init__(self, market_id: int, name: str, short_name: str,
                 image_url: str, url: str, contracts: List[Contract],
                 time_stamp: str, status: str):
        self.id = market_id
        self.name = name
        self.short_name = short_name
        self.image_url = image_url
        self.url = url
        self.contracts = contracts
        self.time_stamp = time_stamp
        self.status = status
