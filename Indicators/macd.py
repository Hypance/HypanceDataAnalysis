import pandas as pd

class MACD:
   
    def __init__(self, data_close):
        self.data_close = data_close
        #we only need to the closure data

    def MovingAverageConvergenceDivergence(self):
   
        #Ema_12 is essential for the MACD, this "12" can be changable, but sorurces take "12".
        #For Ema_12 first we need to mean of first 12 days.
        #Other values of Ema_12 comes from the below calculation. Ema_12 values listed in "for" loop.
        mean_12=sum(self.data_close[0:12])/12
        Ema_12=[mean_12]            
        for i in range(54):
            Ema_12.append(self.data_close[i+12]*(0.15384615384615385)+(Ema_12[i]*(0.8461538461538461)))

        #Ema_26 is essential for the MACD, this "26" can be changable, but sources take "26". 
        #For Ema_26 first we need to mean of first 26 days.
        #Other values of Ema_26 comes from the below calculation. Ema_26 values listed in "for" loop.
        mean_26=sum(data_close[0:26])/26
        Ema_26=[mean_26]
        for i in range(40):
            Ema_26.append(self.data_close[i+26]*(0.07407407407407407)+(Ema_26[i]*(0.9259259259259259)))
   
   
        #MACD values calculated with (Ema_12 - Ema_26). 
        #Datas must be taken from the same day. Because of that i add "14" for Ema_12 values.
        calc_MACD=[]
        for i in range(41):
            calc_MACD.append(Ema_12[14+i]-Ema_26[i])
   
        #For Signal values, first value is the mean of first 9 MACD values.
        #Other values of Signal comes from the below calculation.
        signal_mean=sum(calc_MACD[0:9])/9
        Signal=[signal_mean]
        for i in range(32):
            Signal.append(calc_MACD[i+9]*(0.2)+(Signal[i]*(0.8)))
   
        #Same day of MACD(starting from 8) and Signal values we calculate Histogram values with (MACD - Signal).
        Histogram=[]
        for i in range(33):
            Histogram.append(calc_MACD[8+i]-Signal[i])
   
        #If histogram value turns negative to positive that mean we can buy the stock, else we can sell the stock. 
        #In this code these are printed.
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
       
        return df[33:].reset_index()

#data_close is the closure data. Then we put this data(list type) and print the result. 
#This result is the matrix of the all calculations starting from day 33. 
print(MACD(data_close).MovingAverageConvergenceDivergence())
