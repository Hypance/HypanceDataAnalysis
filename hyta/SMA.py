import pandas as pd     # needs pip install if not installed
 
class Sma:

    def __init__(self,close):
        self.df=pd.DataFrame(data={"close":close})


    def Sma(self):
        df = pd.DataFrame([self.df])
        # calculate 3 moving average using Pandas
        df['3sma'] = df['close'].rolling(3).mean()
        # calculate 5 moving average using Pandas
        df['5sma'] = df['close'].rolling(5).mean()
        return df
