import pandas as pd     
 
class SMA:
    def __init__(self,close,period=5):
        self.df=pd.DataFrame(data={"close":close})
        self.period=period

    def Sma(self):
        # calculate given period moving average using Pandas
        self.df['sma'] = self.df['close'].rolling(self.period).mean()
        return self.df['sma']
