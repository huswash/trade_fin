import pandas as pd
import numpy as np
import pandas_datareader.data as pdr
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm
import statsmodels.regression.rolling as rolOLS
import sklearn as sk
# import PyPortfolioOpt as ppo


SP_res = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
SP_res['Symbol'] = SP_res['Symbol'].str.replace('.', '-')

list_500 = SP_res["Symbol"].unique().tolist()

end_date = dt.datetime.now().date()
start_date = end_date - dt.timedelta(days=365*10)

dframe = yf.download(list_500, start=start_date, end=end_date).stack()
