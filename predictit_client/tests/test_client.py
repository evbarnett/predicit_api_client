import unittest

import time
from predictit_client.client import Client
from predictit_client.market import Market


class TestClient(unittest.TestCase):

    def test_client_single(self):
        """Fetches a single market."""
        time.sleep(1)  # rate limiting
        market_id = 2721
        client = Client()
        market = client.get_market_with_id(market_id)
        self.assertEqual(market_id, market.id)
        self.assertIsNotNone(market)

    def test_fetch_all_markets(self):
        """Fetches all markets."""
        time.sleep(1)  # rate limiting
        client = Client()
        markets = client.get_all_markets()
        self.assertIsNotNone(markets)
        self.assertIsInstance(markets, list)
        self.assertGreater(len(markets), 0)
