#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

class MACD:
   
    def __init__(self, data_close):
        self.data_close = data_close

    def MovingAverageConvergenceDivergence(self,data_close):
   
        #Ema_12 için ilk değer ilk 12 günün ortalaması olacak.
        #Diğer değerler aşağıdaki fonksiyona göre hesaplanmaktadır.
        ortalama_12=sum(self.data_close[0:12])/12
        Ema_12=[ortalama_12]            
        for i in range(54):
            Ema_12.append(self.data_close[i+12]*(0.15384615384615385)+(Ema_12[i]*(0.8461538461538461)))

        #Ema_26 için ilk değer ilk 26 günün ortalaması olacak.
        #Diğer değerler aşağıdaki fonksiyona göre hesaplanmaktadır.
        ortalama_26=sum(data_close[0:26])/26
        Ema_26=[ortalama_26]
        for i in range(40):
            Ema_26.append(self.data_close[i+26]*(0.07407407407407407)+(Ema_26[i]*(0.9259259259259259)))
   
   
        #MACD için değerler aynı güne ait Ema_12 ve Ema_26 değerlerinin farkı alınarak hesaplanmaktadır.
        calc_MACD=[]
        for i in range(41):
            calc_MACD.append(Ema_12[14+i]-Ema_26[i])
   
        #Signal için ilk değer ilk 9 günün MACD verilerinin ortalamsıdır.
        #Diğer değerler aşağıdaki fonksiyona göre hesaplanmaktadır.
        signal_ort=sum(calc_MACD[0:9])/9
        Signal=[signal_ort]
        for i in range(32):
            Signal.append(calc_MACD[i+9]*(0.2)+(Signal[i]*(0.8)))
   
        #Histogram için aynı güne ait MACD ve Signal değerlerinin farkı alınarak hesaplama yapılmaktdır.
        Histogram=[]
        for i in range(33):
            Histogram.append(calc_MACD[8+i]-Signal[i])
   
        for i in range(32):
            if Histogram[i+1]>0 and Histogram[i]<0:
                print("Date of "+f"{i+1}","Buy")
            elif Histogram[i+1]<0 and Histogram[i]>0:
                print("Date of "+f"{i+1}","Sell")
       
        d = {
            "Close": data_close,
            "Ema_12": pd.Series(Ema_12, index=[i for i in range(11,66)]),
            "Ema_26": pd.Series(Ema_26, index=[i for i in range(25,66)]),
            "MACD": pd.Series(calc_MACD, index=[i for i in range(25,66)]),
            "Signal": pd.Series(Signal, index=[i for i in range(33,66)]),
            "Histogram": pd.Series(Histogram, index=[i for i in range(33,66)])
            }
        df=pd.DataFrame(data=d, index=[i for i in range(66)])
       
        return df



path=r"/Users/anilmehmetuyar/Downloads/MACD-Data.xlsx"
data=pd.read_excel(path)
data_close = data['Close'].to_list()
Result=MACD(data_close)
print(Result.MovingAverageConvergenceDivergence(data_close))


# In[ ]:




