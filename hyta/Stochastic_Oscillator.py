
import pandas as pd

class StochasticOscillator:

    def __init__(self,list,periods:int=5):
        self.list=list
        self.periods=periods

    def add_stochastic_oscillator(self):
        df = pd.DataFrame([self.list])

        high_roll = df["High"].rolling(self.periods).max()
        low_roll = df["Low"].rolling(self.periods).min()

    # Fast stochastic indicator
        num = df["Close"] - low_roll
        denom = high_roll - low_roll
        df["%K"] = (num / denom) * 100

    # Slow stochastic indicator
        df["%D"]= df["%K"].rolling(3).mean()
        return df["%D"]
    
    def print(self):
        return self.add_stochastic_oscillator()


