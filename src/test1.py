from lumibot.brokers import Alpaca
from lumibot.strategies.strategy import Strategy
from lumibot.backtesting import YahooDataBacktesting
from lumibot.traders import Trader
from datetime import datetime as dt
from datetime import timedelta
from alpaca_trade_api.rest import REST

API_KEY = " "
SECRET_KEY = " "
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CONFIG = {
    "api_key": API_KEY,
    "secret_key": SECRET_KEY,
    "Paper": True,
}

#class MLTrader(Strategy):
#    def __init__(self, broker, symbol, timeframe, start, end):
#        super().__init__(broker, symbol, timeframe, start, end)
#        self.broker = broker
#        self.symbol = symbol
#        self.timeframe = timeframe
#        self.start = start
#        self.end = end

#    def on_open(self):
#        print("Opening Position")
#        self.broker.buy(self.symbol, 1)

#    def on_close(self):
#        print("Closing Position")
#        self.broker.sell(self.symbol, 1)

#    def on_bar(self, bar):
#        print(bar)

#    def on_tick(self, tick):
#        print(tick)

#    def on_message(self, message):
#        print(message)

#    def on_error(self, error):
#        print(error)

#    def on_exit(self):
#        print("Exiting")

class MLTrader(Strategy):
    def initialize(self, symbol: str="SPY", cash_at_risk:float=.5):
        self.symbol = symbol
        self.sleeptime = "1D"
        self.broker = broker
        self.last_trade = None
        self.cash_at_risk = cash_at_risk
        self.api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)


    def position_size(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        quantity = round(cash * self.cash_at_risk / last_price, 0)
        return cash, last_price, quantity
    
    def get_dates(self):
        today = dt.now()
        date_days_before = today - timedelta(days=3)
        return today.strftime("%Y-%m-%d"), date_days_before.strftime("%Y-%m-%d")
    


    def get_news(self):
        today, date_days_before = self.get_dates()
        news = self.api.get_news(symbol = self.symbol, 
                                 start = date_days_before, 
                                 end = today)
        news = [ev.__dict__ ["_raw"]["headline"]for ev in news]
                
        return news

    def on_trading_iteration(self):
        cash, last_price, quantity = self.position_size()
        if cash > last_price:
            news = self.get_news()
            print(news)
            
            if self.last_trade == None:
                order = self.create_order(
                    self.symbol, 
                    10, 
                    "buy", 
                    type="bracket",
                    take_profit_price=last_price * 1.15,
                    stop_loss_price=last_price * .85,
                )

                self.submit_order(order)
                self.last_trade = "buy"

            

broker = Alpaca(ALPACA_CONFIG)
strategy = MLTrader(name = "mstrat", broker = broker, 
                    parameters = {"symbol":"SPY", 
                                  "cash_at_risk":.5})

start_date = dt(2021, 12, 1)
end_date = dt(2023, 1, 21)

strategy.backtest(
    start = start_date,
    end = end_date,
    symbol = "AAPL",
    timeframe = "1D",
    capital_base = 10000,
    data_frequency = "daily",
    data = YahooDataBacktesting,
    live = False,
    )


def hello():
    print("Hello World!")