import pandas as pd
import numpy as np
 
class ATR:
    '''
    This class calculates ATR for default True_Value=14.
    True_Value 
    data_all=np.array([data_high,data_low,data_close]) data comes with this format.
    
    Attributes
    --------------- 
    data_all  : np.array    
    True_Value: int
    '''
    
    def __init__(self, data_all, true_value=14):
        self.data_all = data_all
        self.true_value=true_value
       
    def TrueRange(self) -> list:
        
        #listing the absolute value of the each all_data.
        #closing data comes from the day before.
        tr=[abs(data_all[0][0]-data_all[1][0])]            
        for i in range(1,len(data_all[2])):
            tr.append(max(abs(data_all[2][i-1]-data_all[0][i]),
                         abs(data_all[2][i-1]-data_all[1][i]),
                         abs(data_all[0][i]-data_all[1][i])))
        
        return tr
    
    def AverageTrueRange(self) -> list:
        #Listing the avarage true range.
        atr=[np.mean(self.TrueRange()[:self.true_value])]
        for i in range(len(data_all[2])-self.true_value):
            atr.append((atr[i]*(self.true_value-1)+self.TrueRange()[i+self.true_value])/self.true_value)
    
        return atr