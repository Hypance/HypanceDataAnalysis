
import pandas as pd
data=pd.read_excel('Stochastic-Oscillator.xlsx')
print(data)

def add_stochastic_oscillator(df, periods=5):
    copy = df.copy()
    
    high_roll = copy["High"].rolling(periods).max()
    low_roll = copy["Low"].rolling(periods).min()
    
    # Fast stochastic indicator
    num = copy["Close"] - low_roll
    denom = high_roll - low_roll
    copy["%K"] = (num / denom) * 100
    
    # Slow stochastic indicator
    copy["%D"] = copy["%K"].rolling(3).mean()
    
    return copy
