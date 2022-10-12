import pandas as pd

class CMF:

    """
    This class calculate the cmf for 20 period.
    ...
    Attributes
    ----------
    close : pandas.Series
    low : pandas.Series
    high : pandas.Series
    volume: pandas.Series

    Methods
    -------
    money_flow_multiplier(close,low,high):
        Returns the mfm.

    money_flow_volume(mfm, volume):
        Returns the mfv.

    cmf(money_flow_multiplier,money_flow_volume,data):
        Returns the cmf. 

    """
    
    def __init__(self,close:pd.Series,low:pd.Series,high:pd.Series,volume:pd.Series,period=20):
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        self.period = period
        
    def money_flow_multiplier(self):
        mfm = ((self.close - self.low) - (self.high - self.close)) / (self.high - self.low)
        try:
            self.low/self.high
        except ZeroDivisionError as e:
            return "There is a data problem."
            
        return mfm

    def money_flow_volume(self):
        mfv = self.mfm * self.volume
        return mfv
    
    def cmf(self):
        close = self.close
        low = self.low
        high = self.high
        volume = self.volume
        period = self.period

        mfm = self.money_flow_multiplier(close,low,high)
        mfv = self.money_flow_volume(mfm,volume)
        cmf = mfv.rolling(window=period).sum() / volume.rolling(window=period).sum()
        return cmf