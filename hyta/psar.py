#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

class ParabolicSAR:
    
    '''
    This class calculates ParobolicSAR. All initials connected each other.
    SAR means stop and reverse.
    If PSAR point is lower than the actual data it means "BUY" else it means "SELL".
    
    Attributes
    --------------- 
    data_high : list
    data_low : list
    data_close : list
    '''
   
    def __init__(self,data_high:list,data_low:list,data_close:list):
        self.data_high = data_high
        self.data_low = data_low
        self.data_close = data_close
      
    def parabolic_sar(self) -> list:
        
        #first, setting up initial values 
        #ep is a list of extremum points
        ep=[data_low[0]]  
        #psar is a list of parabolic stop and reverse values
        psar=[data_high[0]] 
        #acc point is a accumulation point list
        acc_point=[.02]
        #trend is a list of trend of graphic(falling and rising)
        trend=["Falling"]
        #calc_psar is a list of calculation of below function
        calc_psar=[(psar[0]-ep[0])*acc_point[0]]
        #initial_psar is a list of values determines actual psar
        initial_psar=[]
        
        for i in range(len(data_high)-1):
            #setting initial psar values according to trend
            if trend[i]=="Falling":
                try:
                    initial_psar.append(max((psar[i]-calc_psar[i]),np.array(data_high[i-1:i+1]).max()))
                except ValueError:
                    initial_psar.append(max((psar[i]-calc_psar[i]),np.array(data_high[0:1]).max()))
            elif trend[i]=="Rising":
                try:
                    initial_psar.append(min((psar[i]-calc_psar[i]),np.array(data_low[i-1:i+1]).min()))
                except ValueError:
                    initial_psar.append(max((psar[i]-calc_psar[i]),np.array(data_low[0:1]).min()))
                    
            #setting psar values according to trend,initial_psar and data 
            if trend[i]=="Falling" and data_high[i+1]<initial_psar[i]:
                psar.append(initial_psar[i])
            elif trend[i]=="Falling" and data_high[i+1]>=initial_psar[i]:
                psar.append(ep[i])
            elif trend[i]=="Rising" and data_low[i+1]>initial_psar[i]:
                psar.append(initial_psar[i])
            elif trend[i]=="Rising" and data_low[i+1]<=initial_psar[i]:
                psar.append(ep[i])
                
            #decide on the trend according to psar and close data
            if psar[i+1]>data_close[i+1]:
                trend.append("Falling")
            else:
                trend.append("Rising")
                
            #setting extremum point    
            if trend[i+1]=="Falling":
                ep.append(min(ep[i],data_low[i+1]))
            else:
                ep.append(max(ep[i],data_high[i+1]))
                
            #decide on the accumulation point    
            if trend[i]==trend[i+1] and ep[i]!=ep[i+1] and acc_point[i]<0.2:
                acc_point.append(.02+acc_point[i])
            elif trend[i]==trend[i+1] and ep[i]==ep[i+1]:
                acc_point.append(acc_point[i])
            elif trend[i]!=trend[i+1]:
                acc_point.append(acc_point[0])
            else:
                acc_point.append(.2)
            
            #decide on the result of ((psar-ep)*acc_point)   
            calc_psar.append((psar[i+1]-ep[i+1])*acc_point[i+1])

                
        return psar
    


path=r"/Users/anilmehmetuyar/Downloads/PSAR.xlsx"
data=pd.read_excel(path)
data_close = data['Close'].to_list()
data_high = data['High'].to_list()
data_low = data['Low'].to_list()
print(ParabolicSAR(data_high,data_low,data_close).parabolic_sar())


# In[ ]:




