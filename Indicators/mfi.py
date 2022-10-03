import pandas as pd

class MFI:
    """
    This class calculate the money flow index for specific period.
    ...
    Attributes
    ----------
    close : list
    low : list
    high : list
    volume: list

    Methods
    -------
    typical_price(high,low,close):
        Returns the typical price.

    raw_money_flow(volume,typical_price):
        Returns the raw money flow.
        
    positive_money_flow(period:int,data):
        Returns the positive money flow. 
    
    negative_money_flow(period:int,data):
        Returns the negative money flow.
    
    money_ratio(positive_money_flow, negative_money_flow,period):
        Returns the money ratio.
    
    money_flow_index(money_ratio):
        Return the money flow index (mfi)
    """

    def __init__(self,close:list,low:list,high:list,volume:list,data):
            self.close = close
            self.low = low
            self.high = high
            self.volume = volume
            self.data = data
            
    def typical_price(high,low,close):
        return (high + low + close) / 3

    def raw_money_flow(volume,typical_price):
        return volume * typical_price
    
    def positive_money_flow(period:int,data):
        positive_mf = data["1-period Positive Money Flow"].rolling(window=period).sum()
        return positive_mf

    def negative_money_flow(period:int,data):
        negative_mf = data["1-period Negative Money Flow"].rolling(window=period).sum()
        return negative_mf
    
    def money_ratio(positive_money_flow, negative_money_flow,period):
        return positive_money_flow(period) / negative_money_flow(period)
    
    def money_flow_index(money_ratio):
        mfi =  100 - 100 / (1 + money_ratio)
        return mfi