
import pandas as pd

class StochasticOscillator:

    def __init__(self,list,periods:int=5):
        self.list=list
        self.periods=periods

    def High_Low_Stoch(self):
        df = pd.DataFrame([self.list])

        high_roll = df["High"].rolling(self.periods).max()
        low_roll = df["Low"].rolling(self.periods).min()
        return df

    # Fast stochastic indicator
    
    def Fast_Stochastic():
        num = df["Close"] - low_roll
        denom = high_roll - low_roll
        df["%K"] = (num / denom) * 100
        return  df["%K"]

    # Slow stochastic indicator
    
    def Slow_Stochastic():
        df["%D"]= df["%K"].rolling(3).mean()
        return df["%D"]
    
    def StochasticOscillator(self):
        return self.High_Low_Stoch()


