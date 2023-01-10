
import pandas as pd


class StochasticOscillator:

    def __init__(self,high,low,close,periods=5):
        self.periods=periods
        self.df=pd.DataFrame(data={"high":high,"low":low,"close":close})
        
           
    def high_low_stoch(self):
        self.df["high_roll"] = self.df["high"].rolling(self.periods).max()
        self.df["low_roll"] = self.df["low"].rolling(self.periods).min()
        return self.df
        

    # Fast stochastic indicator
    
    def fast_stochastic(self):
        self.high_low_stoch()      
        num = self.df["close"] - self.df["low_roll"]
        denom = self.df["high_roll"]-self.df["low_roll"]
        self.df["%K"] = (num / denom) * 100
        return self.df["%K"]
    
        
    # Slow stochastic indicator
    
    def slow_stochastic(self):
        self.fast_stochastic()
        self.df["%D"]= df["%K"].rolling(3).mean()
        return df["%D"]

