from alpaca.data.live import StockDataStream
from alpaca.data.live import CryptoDataStream

data_stream = StockDataStream("956KDWQDK7KH760", "lAb8IJMhTMhwOvhvbMUdTO33VHqfcE")

async def handle_data(data):
    print(data)

data_stream.subscribe( handle_data, "GOOGL")
data_stream.run()

data_stream_ = CryptoDataStream("","")
async def handle_data_(data):
    print(data)

data_stream_.subscribe( handle_data_, "BTC/USD")
data_stream_.run()
