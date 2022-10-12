from cmath import nan
import numpy as np


class MA:
    '''
    This class calculates MA for default 3-days period.
    Attributes
    --------------- 
    close : list
    period : int
    '''
    def __init__(self,dataset:list,period:int=3):
        self.dataset = dataset
        self.period = period
    
    
    # Calculating the mean
    # for a given period (Default: 3 days)

    def calcAverage(self):                             
        ret = np.cumsum(self.dataset,dtype=float)      
        ret[self.period:] = ret[self.period:] - ret[:-self.period]
        return ret[self.period-1:] / self.period


     # Inserting the NaNs to the list
     # by using this function.    
    
    def nanSeries(self):
        nanSeri=[]
        for _ in range(self.period):                      
           nanSeri.append(nan)                           
        nanSeri[(self.period-1):] = self.calcAverage()
        return nanSeri

    def ma(self) -> list:
        return self.nanSeries()  

