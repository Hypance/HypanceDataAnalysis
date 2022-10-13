import os
from binance.client import Client
import pprint
import pandas as pd     # needs pip install if not installed
import numpy as np
import matplotlib.pyplot as plt   # needs pip install if not installed

#designing SMA bot 


    ''''valid intervals-1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 
    1w, 1M request historical candle (or klines) data using timestamp from above 
    interval either every min, hr, day or month
    starttime = '30 minutes ago UTC' for last 30 mins time
    e.g. client.get_historical_klines(symbol='ETHUSDTUSDT', '1m', starttime)
    starttime = '1 Aug, 2012', '12 Sep, 2012'  for one month of 2012
    e.g. client.get_historical_klines(symbol='BTCUSDT', '1m', "1 Aug, 2012", 
    # "12 Sep, 2012"). #These intervals, the symbols of historical klines and 
    start time are changeable considering data worksheet'''
 
    starttime = '1 Aug 2012'  # start date
    interval = '1h'
  
    bars = client.get_historical_klines(symbol, interval, starttime) 
 
    # Keep only first 5 columns, "date" "open" "high" "low" "close"
    for line in bars:
        del line[5:]
    #  2 dimensional tabular data
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])   
    return df

class Sma:

    def__init__(self,data,smaPeriod):
        self.data=data
        self.smaPeriod=smaPeriod

    def __get_hourly_dataframe():

    
    def main():
        Sma()

    def Sma():
        symbol_df = __get_hourly_dataframe()
        # calculate 5 moving average using Pandas
        symbol_df['5sma'] = symbol_df['close'].rolling(5).mean()
        # calculate 15 moving average using Pandas
        symbol_df['15sma'] = symbol_df['close'].rolling(15).mean()
