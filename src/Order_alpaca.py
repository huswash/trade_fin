from alpaca.trading.client import TradingClient

client = TradingClient("PK7DWQDDDH8KH760956K",
                       "hAM5zdaFkPlAb8IJMhTMhwOvhvbMUdTO33VHqfcE", None,
                       True,)

print(client.get_account().account_number)
print(client.get_account().buying_power)

from alpaca.data import StockHistoricalDataClient, StockTradesRequest
import datetime as dt

data_alpaca = StockHistoricalDataClient("PK7DWQDDDH8KH760956K", "hAM5zdaFkPlAb8IJMhTMhwOvhvbMUdTO33VHqfcE")

request_params = StockTradesRequest(
    symbol_or_symbols = "MSFT",
    start=dt.datetime(2024, 1, 30, 14, 30),
    end=dt.datetime(2024, 1, 30, 14, 45)
    )  
trades = data_alpaca.get_stock_trades(request_params)

for trades in trades.data["MSFT"]:
    print(trades)
    break