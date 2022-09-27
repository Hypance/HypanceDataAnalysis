
import pandas as pd

class stochastic_oscillator:
    def __init__(self,list,periods:int=5):
        self.list=list
        self.periods=periods

    def add_stochastic_oscillator(self):
        df = pd.DataFrame([self.list])

        high_roll = copy["High"].rolling(self.periods).max()
        low_roll = copy["Low"].rolling(self.periods).min()

    # Fast stochastic indicator
        num = copy["Close"] - low_roll
        denom = high_roll - low_roll
        copy["%K"] = (num / denom) * 100

    # Slow stochastic indicator
        return copy["%D"]= copy["%K"].rolling(3).mean()

    def print(self):
        return self.add_stochastic_oscillator()

stochastic_oscillator(list).print()
