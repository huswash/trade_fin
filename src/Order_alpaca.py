from alpaca.trading.client import TradingClient

client = TradingClient("",
                       "", None,
                       True,)

print(client.get_account().account_number)
print(client.get_account().buying_power)

from alpaca.data import StockHistoricalDataClient, StockTradesRequest
import datetime as dt

data_alpaca = StockHistoricalDataClient("", "")

request_params = StockTradesRequest(
    symbol_or_symbols = "MSFT",
    start=dt.datetime(2024, 1, 30, 14, 30),
    end=dt.datetime(2024, 1, 30, 14, 45)
    )  
trades = data_alpaca.get_stock_trades(request_params)

for trades in trades.data["MSFT"]:
    print(trades)
    break

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, OrderType, TimeInForce
from alpaca.trading.requests import MarketOrderRequest

TradeCL = TradingClient("", "", None, True)

order_data = MarketOrderRequest(
    symbol="AAPL", 
    qty=400, 
    side=OrderSide.BUY, 
    time_in_force=TimeInForce.DAY)

subt_order = TradeCL.submit_order(order_data)
print(subt_order)