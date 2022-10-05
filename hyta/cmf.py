import pandas as pd

class CMF:

    """
    This class calculate the cmf for 20 period.
    ...
    Attributes
    ----------
    close : pd.Series
    low : pd.Series
    high : pd.Series
    volume: pd.Series

    Methods
    -------
    money_flow_multiplier(close,low,high):
        Returns the mfm.

    money_flow_volume(mfm, volume):
        Returns the mfv.

    cmf(money_flow_multiplier,money_flow_volume,data):
        Returns the cmf. 

    """
    
    def __init__(self,close:pd.Series,low:pd.Series,high:pd.Series,volume:pd.Series,data):
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        self.data = data
        
    def money_flow_multiplier(close,low,high):
        mfm = ((close - low) - (high - close)) / (high - low)
        return mfm

    def money_flow_volume(mfm, volume):
        mfv = mfm * volume
        return mfv
    
    def cmf(money_flow_multiplier,money_flow_volume,data):
        mfm = money_flow_multiplier(data.loc[:,"Close"],data.loc[:,"Low"],data.loc[:,"High"])
        mfv = money_flow_volume(mfm, data.loc[:, "Volume"])
        cmf = mfv.rolling(window=20).sum() / data["Volume"].rolling(window=20).sum()
        return cmf

