class Contract:

    def __init__(self,
                 contract_id: int, date_end: str, image_url: str,
                 name: str, short_name: str, status: str,
                 last_trade_price: float, best_buy_yes_cost: float, best_buy_no_cost: float,
                 best_sell_yes_cost: float, best_sell_no_cost: float, display_order: int
                 ):
        self.id = contract_id
        self.date_end = date_end
        self.image_url = image_url
        self.name = name
        self.short_name = short_name
        self.status = status
        self.last_trade_price = last_trade_price
        self.best_buy_yes_cost = best_buy_yes_cost
        self.best_buy_no_cost = best_buy_no_cost
        self.best_sell_yes_cost = best_sell_yes_cost
        self.best_sell_no_cost = best_sell_no_cost
        self.display_order = display_order
