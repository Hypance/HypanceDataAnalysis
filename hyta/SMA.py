import pandas as pd     
 
class SMA:

    def __init__(self,close,period):
        self.df=pd.DataFrame(data={"close":close})
        self.period=period


    def Sma(self):
        df = pd.DataFrame([self.df])
        # calculate given period moving average using Pandas
        df['sma'] = df['close'].rolling(self.period).mean()
        return df['sma']
