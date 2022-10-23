import os
from binance.client import Client
import pprint
import pandas as pd     # needs pip install if not installed
import numpy as np
import matplotlib.pyplot as plt   # needs pip install if not installed
 

class Sma:

    def __init__(self,data,smaPeriod):
        self.data=data
        self.smaPeriod=smaPeriod

    def __get_hourly_dataframe():
        pass

    
    def main():
        Sma()

    def Sma():
        symbol_df = __get_hourly_dataframe()
        # calculate 5 moving average using Pandas
        symbol_df['5sma'] = symbol_df['close'].rolling(5).mean()
        # calculate 15 moving average using Pandas
        symbol_df['15sma'] = symbol_df['close'].rolling(15).mean()

