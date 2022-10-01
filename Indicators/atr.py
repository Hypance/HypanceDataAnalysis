import pandas as pd
import numpy as np
 
class ATR:
    #data_all=np.array([data_close,data_high,data_low]) data comes with this format.
    
    def __init__(self, data_all):
        self.data_all = data_all
       
 
    def AverageTrueRange(self,data_all):
    
        #True Range için yapılacak hesaplamaları TR listesine atalım.
        TR=[abs(data_all[1][0]-data_all[2][0])]            
        for i in range(1,30):
            TR.append(max(abs(data_all[0][i-1]-data_all[1][i]),
                          abs(data_all[0][i-1]-data_all[2][i]),
                          abs(data_all[1][i]-data_all[2][i])))
             
        ATR=[]
        ATR.append(np.mean(TR[0:14]))
        for i in range(16):
            ATR.append((ATR[i]*13+TR[i+14])/14)

        return ATR
