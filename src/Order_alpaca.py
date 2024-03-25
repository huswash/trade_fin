# from alpaca.trading.client import TradingClient

# client = TradingClient("PK7DWQDDDH8KH760956K",
#                        "hAM5zdaFkPlAb8IJMhTMhwOvhvbMUdTO33VHqfcE", None,
#                       True,)

# print(client.get_account().account_number)
# print(client.get_account().buying_power)

# from alpaca.data import StockHistoricalDataClient, StockTradesRequest
# import datetime as dt

# data_alpaca = StockHistoricalDataClient("PK7DWQDDDH8KH760956K", "hAM5zdaFkPlAb8IJMhTMhwOvhvbMUdTO33VHqfcE")

# request_params = StockTradesRequest(
#     symbol_or_symbols = "MSFT",
#     start=dt.datetime(2024, 1, 30, 14, 30),
#     end=dt.datetime(2024, 1, 30, 14, 45)
#     )  
# trades = data_alpaca.get_stock_trades(request_params)

# for trades in trades.data["MSFT"]:
#     print(trades)
#     break

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, OrderType, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest, GetOrdersRequest

TradeCL = TradingClient("PK7956K", "hAMO33VHqfcE", None, True)

# order_data = MarketOrderRequest(
#     symbol="AAPL", 
#     qty=400, 
#     side=OrderSide.BUY, 
#     time_in_force=TimeInForce.DAY)

# subt_order = TradeCL.submit_order(order_data)
# print(subt_order)

order_data_ = LimitOrderRequest(
    symbol="GOOGL", 
    qty=40, 
    side=OrderSide.BUY, 
    time_in_force=TimeInForce.DAY,
    limit_price= 145.00
)

lsu_order = TradeCL.submit_order(order_data_)
print(lsu_order)

request_params_ = GetOrdersRequest(
    status=QueryOrderStatus.OPEN
)

_orders_ = TradeCL.get_orders(request_params_)
for order in _orders_:
    print(order )

positions = TradeCL.get_all_positions()

for position in positions:
    print(position.symbol, position.current_price)