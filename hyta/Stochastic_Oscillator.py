
import pandas as pd



class StochasticOscillator:

    def __init__(self,high,low,close,periods=5):
        self.periods=periods
        self.df=pd.DataFrame(data={"high":high,"low":low,"close":close})
        
           
    def high_low_stoch(self):
        
        df["high_roll"] = self.df["high"].rolling(self.periods).max()
        df["low_roll"] = self.df["low"].rolling(self.periods).min()
        return df

    # Fast stochastic indicator
    
    def fast_stochastic(self):
        df=self.high_low_stoch()      
        num = df["close"] - df["low_roll"]
        denom = df["high_roll"]-df["low_roll"]
        df["%K"] = (num / denom) * 100
        return  df["%K"]

    # Slow stochastic indicator
    
    def slow_stochastic(self):
        df["%K"]=self.fast_stochastic()
        df["%D"]= df["%K"].rolling(3).mean()
        return df["%D"]

