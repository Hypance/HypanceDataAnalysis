import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Bollinger:
    '''
    Class for calculating bollinger bands
    '''
    def __init__(self,df,close):
        self.df =df
        self.close = close


    def bands(self):
        df = pd.DataFrame()
        
        #Simple moving average and standart deviation
        # based on closing values of the last 20 days.  
        df["SMA"] = self.close.rolling(window = 20).mean()
        df["stddev"] = self.close.rolling(window = 20).std()

        df["Upper"] = df["SMA"] + 2 * df["stddev"]
        df["Lower"] = df["SMA"] - 2 * df["stddev"]
        
        return df["Close"],df["Upper"],df["Close"]





