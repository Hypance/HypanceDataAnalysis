from cmath import nan
import numpy as np


class movingAverage:
    def __init__(self,dataset:list,period:int=3):
        self.dataset = dataset
        self.period = period

    def calcAverage(self):                             # Calculating the mean
        ret = np.cumsum(self.dataset,dtype=float)      # for a given period
        ret[self.period:] = ret[self.period:] - ret[:-self.period]
        return ret[self.period-1:] / self.period


    def nanSeries(self):
        nanSeri=[]
        for _ in range(self.period):                      # Inserting the NaNs to the list
           nanSeri.append(nan)                            # by using this function.
        nanSeri[(self.period-1):] = self.calcAverage()
        return nanSeri

    def print(self) -> list:
        return self.nanSeries()

# movingAverage('dataset','period').print() for running.

    
      


