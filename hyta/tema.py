import pandas as pd
import numpy as np

class TEMA:
    
    '''
    This class calculates Triple Exponential Moving Average Indicator for given close data and 
    period(must be positive integer).
    
    When the close data is beyond the TEMA, it assists secure an uptrend.
    When the close data is below the TEMA, it helps confirm a downtrend.
    
    Attributes
    --------------- 
    close  : pd.Series
    period : int
    '''
   
    def __init__(self, close:pd.Series, period:int=3):
        self.close = close
        self.period=period
        
        #multiplier is float value between 0 and 1.
        self.multiplier=2/(1+period)
    
    
    # calculating simple moving average for given period.
    def simple_moving_average(self) -> pd.Series:
        
        data['SMA']=self.close.rolling(window=self.period).mean()
        
        return data['SMA']
    
    
    # respectively calculating exponential moving averages
    def ema_1(self) -> list:
        
        ema1=[(self.close[self.period-1]*self.multiplier)+(self.simple_moving_average()[self.period-1]*(1-self.multiplier))]
        
        for i in range(len(self.close)-self.period):
            ema1.append((self.close[i+self.period]*self.multiplier)+(ema1[i]*(1-self.multiplier)))

        return ema1
       
        
    def ema_2(self) -> list:
        
        ema2=[(self.ema_1()[0]*self.multiplier)+(self.simple_moving_average()[self.period-1]*(1-self.multiplier))]
        
        for i in range(len(self.close)-self.period):
            ema2.append((self.ema_1()[i+1]*self.multiplier)+(ema2[i]*(1-self.multiplier)))

        return ema2
    
    
    def ema_3(self) -> list:
        
        ema3=[(self.ema_2()[0]*self.multiplier)+(self.simple_moving_average()[self.period-1]*(1-self.multiplier))]
        
        for i in range(len(self.close)-self.period):
            ema3.append((self.ema_2()[i+1]*self.multiplier)+(ema3[i]*(1-self.multiplier)))

        return ema3
    
    
    #finally, calculating triple exponential moving average values.
    #In that case, pandas series used.
    def tema(self) -> pd.Series:
        d = {
        "EMA1": pd.Series(self.ema_1()),
        "EMA2": pd.Series(self.ema_2()),
        "EMA3": pd.Series(self.ema_3())
        }
        d['triple_exponential_moving_average']=3*d['EMA1']-3*d['EMA2']+d['EMA3']
        
        return d['triple_exponential_moving_average']