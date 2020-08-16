# PredictIt API Client

[![python-unittest Actions Status](https://github.com/evbarnett/predictit-client/workflows/python-unittest/badge.svg?branch=master)](https://github.com/evbarnett/predictit-client/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PredictIt API Client for Python. Python 3+ required.

## Installation

`pip install predictit-client`

## Usage

```python
from predictit_client import Client
```

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
market = client.get_market_with_id(market_id) # -> Optional[Market]
```

**Market Fields**

```python
market_id: int  
name: str  
short_name: str  
image_url: str  
url: str  
contracts: List[Contract]  
time_stamp: str  
status: str
```

**Contract Fields**

```python
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
```
