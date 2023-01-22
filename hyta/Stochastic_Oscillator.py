
import pandas as pd

class StochasticOscillator:
    def __init__(self, high, low, close, periods: int = 5):
        self.high = high
        self.low = low
        self.close = close
        self.periods = periods
        self.df = pd.DataFrame(
            {"High": self.high, "Low": self.low, "Close": self.close})
        self.high_roll = self.highroll()
        self.low_roll = self.lowroll()
        self.df["%K"] = self.fast_stochastic()
        self.df["%D"] = self.slow_stochastic()

    def highroll(self):
        self.high_roll = self.df["High"].rolling(self.periods).max()
        return self.high_roll

    def lowroll(self):
        self.low_roll = self.df["Low"].rolling(self.periods).min()
        return self.low_roll

    # Fast stochastic indicator

    def fast_stochastic(self):
        num = self.df["Close"] - self.low_roll
        denom = self.high_roll - self.low_roll
        return (num / denom) * 100

    # Slow stochastic indicator
    def slow_stochastic(self):
        return self.df["%K"].rolling(3).mean()

    def stochasticoscillator(self):
        self.fast_stochastic()
        self.slow_stochastic()
        return self.df
