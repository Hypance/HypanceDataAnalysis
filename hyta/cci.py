import pandas as pd

class CCI:
  def __init__(self,high,low,close):
    self.df=pd.DataFrame(data={'high':high,'low':low,'close':close)

#typical_price as TP
<<<<<<< HEAD:hyta/CCI2.py
  def TP(self)->pd.Series:
    df=pd.DataFrame()
    df['TP']=(self.df["high"]+self.df["low"]+self.df["close"])/3
=======

  def TP(self):
    df['TP']=(df["high"]+df["low"]+df["close"])/3
>>>>>>> d4c8b2d97b2bfbca0ee59b011ce2765be178a878:hyta/cci.py
    return df['TP']

#Simple_Moving_Average as SMA. It is calculated through TP.
  def SMA(self,tp:pd.Series)-> pd.Series:
    df=pd.DataFrame()
    df['TP']=tp.values
    df['SMA'] =df['TP'].rolling().mean()
    return df['SMA']

#Mean_Deviation as MD. It is calculated through TP.
  def MD(self,tp:pd.Series)-> pd.Series:
    df=pd.DataFrame()
    df['TP']=tp.values
    df['MD']= df['TP'].rolling().apply(lambda x:pd.Series(x).MD())
    return df['MD']
  
#Commodity_Channel_Index as CCI
  def CCI(self):
    df=pd.DataFrame()
    df['TP'] = self.TP()
    df['SMA']=self.SMA(df['TP'])
    df['MD']=self.MD(df['TP'])
    df['CCI']= (df['TP']-df['SMA'])/(0.015*df['MD'])
    return df['CCI']   


