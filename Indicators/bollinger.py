import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Bollinger-Bands-Copied.xls")

class Bollinger:
    def __init__(self,df,close):
        self.df =df
        self.close = close

    def bands_and_signals(self):
        global df        
        df["SMA"] = self.close.rolling(window = 20).mean()
        df["stddev"] = self.close.rolling(window = 20).std()
        df["Upper"] = df["SMA"] + 1.8 * df["stddev"]
        df["Lower"] = df["SMA"] - 2 * df["stddev"]
        df["BuySignal"] = np.where(df["Lower"] > df["Close"],True,False)
        df["SellSignal"] = np.where(df["Upper"] < df["Close"],True,False)
        
        buys = []
        sells = []
        open_pos = False
        for i in range(len(df)):
            if df["Lower"][i] > df["Close"][i]:
                if open_pos == False:
                    buys.append(i)
                    open_pos = True
            elif df["Upper"][i] < df["Close"][i]:
                if open_pos:
                    sells.append(i)
                    open_pos = False
        return [df,buys,sells]

def plot(bol,buy,sell):
    plt.figure(figsize=(12,6))
    plt.plot(bol[["Close","SMA","Upper","Lower"]])
    plt.fill_between(bol.index,bol["Upper"],bol["Lower"],color = "grey",alpha = 0.3)
    plt.legend(["Close","SMA","Upper","Lower"])
    plt.scatter(bol.iloc[buy].index,bol.iloc[buy].Close,marker="^",color = "g")
    plt.scatter(bol.iloc[sell].index,bol.iloc[sell].Close,marker="v",color = "r")
    return plt.show()

def main():
    bol = Bollinger(df,df["Close"]).bands_and_signals()[0]
    buy = Bollinger(df,df["Close"]).bands_and_signals()[1]
    sell = Bollinger(df,df["Close"]).bands_and_signals()[2]
    plot(bol,buy,sell)

if __name__ == "__main__":
    main()



