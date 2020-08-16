# PredictIt API Client

[![python-unittest Actions Status](https://github.com/evbarnett/predicit_api_client/workflows/python-unittest/badge.svg?branch=master)](https://github.com/evbarnett/predicit_api_client/actions)

PredictIt API Client in Python

## Installation

`pip install predictit_client`

## Usage

**Get all markets**

```python
market_id = 2721
client = Client()
markets = client.get_all_markets() # -> List[Market]
```

**Get single market**

```python
market_id = 2721
client = Client()
market = client.get_market_with_id(market_id) # -> Market
```

**Market Fields**

market_id: int  
name: str  
short_name: str  
image_url: str  
url: str  
contracts: List\[Contract\]  
time_stamp: str  
status: str  

**Contract Fields**

contract_id: int  
date_end: str  
image_url: str  
name: str   
short_name: str  
status: str  
last_trade_price: float  
best_buy_yes_cost: float  
best_buy_no_cost: float  
best_sell_yes_cost: float  
best_sell_no_cost: float  
display_order: int  
