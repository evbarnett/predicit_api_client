from xml.etree.ElementTree import Element
import requests
from .market import Market
from .contract import Contract
from typing import *
import json


class Client:
    """

    MIT, github.com/evbarnett
    """

    def __init__(self):
        self.all_markets_endpoint = "https://www.predictit.org/api/marketdata/all/"
        self.single_market_endpoint = "https://www.predictit.org/api/marketdata/markets/{}"

    def get_all_markets(self) -> List[Market]:
        """TODO."""
        json_str = self._request(self.all_markets_endpoint)
        market_data = json.loads(json_str)
        markets = self._parse_market_list_json(market_data)
        return markets

    def get_market_with_id(self, market_id: int) -> Optional[Market]:
        """TODO."""
        json_str = self._request(self.single_market_endpoint.format(market_id))
        market_data_dict = json.loads(json_str)
        market = self._parse_single_market_dict(market_data_dict)
        if market is not None:
            return market
        return None

    def _request(self, url: str) -> str:
        r = requests.get(url)
        return r.text

    def _parse_market_list_json(self, market_datas: dict) -> List[Market]:
        market_data = market_datas['markets']
        market_list = []
        for m in market_data:
            new_market = self._parse_single_market_dict(m)
            market_list.append(new_market)
        return market_list

    def _parse_single_market_dict(self, market_data: dict) -> Market:
        market_id = market_data['id']
        name = market_data['name']
        short_name = market_data['shortName']
        image = market_data['image']
        url = market_data['url']
        time_stamp = market_data['timeStamp']
        status = market_data['status']
        contracts = market_data['contracts']
        contract_list = []
        for c in contracts:
            contract_list.append(self._parse_contract(c))
        return Market(market_id, name, short_name, image, url, contracts, time_stamp, status)

    def _parse_contract(self, contract: dict) -> Contract:
        print(contract)
        contract_id = contract['id']
        date_end = contract['dateEnd']
        image = contract['image']
        name = contract['name']
        short_name = contract['shortName']
        status = contract['status']
        last_trade_price = contract['lastTradePrice']
        best_buy_yes_cost = contract['bestBuyYesCost']
        best_buy_no_cost = contract['bestBuyNoCost']
        best_sell_yes_cost = contract['bestSellYesCost']
        best_sell_no_cost = contract['bestSellNoCost']
        display_order = contract['displayOrder']
        return Contract(contract_id, date_end, image, name, short_name, status,
                        last_trade_price, best_buy_yes_cost, best_buy_no_cost,
                        best_sell_yes_cost, best_sell_no_cost, display_order)

    def get_all_markets_async(self, callback: Callable[[List[Market]], None]) -> bool:
        """TODO."""
        pass
