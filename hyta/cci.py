import pandas as pd

class CCI:
  def __init__(self,high,low,close):
    self.df=pd.DataFrame(data={'high':high,'low':low,'close':close)

#typical_price as TP

  def TP(self):
    df['TP']=(df["high"]+df["low"]+df["close"])/3
    return df['TP']

#Simple_Moving_Average as SMA. It is calculated through TP.
  
  def SMA(self):
    df = self.TP()
    self.df['TP']=self.TP(self.df)
    df['SMA'] =df['TP'].rolling().mean()
    return df['SMA']

#Mean_Deviation as MD. It is calculated through TP.

  def MD(self):
    df = self.TP()
    self.df['TP']=self.TP(self.df)
    df['MD']= df['TP'].rolling().apply(lambda x:pd.Series(x).MD())
    return df['MD']
  
#Commodity_Channel_Index as CCI

  def CCI(self):
    df['TP'] = self.TP()
    self.df['TP']=self.TP(self.df)
    df['CCI']= (df['TP']-df['SMA'])/(0.015*df['MD'])
    return df['CCI']   

