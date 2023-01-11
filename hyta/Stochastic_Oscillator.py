
import pandas as pd

class StochasticOscillator:

    def __init__(self,high,low,close,periods:int=5):
        self.high=high
        self.low=low
        self.close=close
        self.periods=periods

        self.df = pd.DataFrame({"High":self.high,"Low":self.low,"Close":self.close})

    def high_low_stoch(self):
        self.high_roll = self.df["High"].rolling(self.periods).max()
        self.low_roll = self.df["Low"].rolling(self.periods).min()
        return self.df

    # Fast stochastic indicator
    
    def fast_stochastic(self):
        num = self.df["Close"] - self.low_roll
        denom = self.high_roll - self.low_roll
        self.df["%K"] = (num / denom) * 100
        return  self.df["%K"]

    # Slow stochastic indicator
    
    def slow_stochastic(self):
        self.df["%D"]= self.df["%K"].rolling(3).mean()
        return self.df["%D"]
    
    def stochastic_oscillator(self):
        return self.high_low_stoch()


