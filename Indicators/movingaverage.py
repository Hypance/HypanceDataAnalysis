from cmath import nan
import numpy as np


class movingAverage:
    def __init__(self,dataset,period=3):
        self.dataset = dataset
        self.period = period

    def calcAverage(self):         # n değeri yerine girilen sayılık günlük ortalama bulduruyor
        ret = np.cumsum(self.dataset,dtype=float)
        ret[self.period:] = ret[self.period:] - ret[:-self.period]
        return ret[self.period-1:] / self.period


    def nanSeries(self):
        nanSeri=[]
        for _ in range(self.period):
           nanSeri.append(nan) #istediğimiz vakitten itibaren ortalamanın plot için gerekli boşlukları sağlayacak
        nanSeri[(self.period-1):] = self.calcAverage()
        return nanSeri

    def yazdir(self) -> list:
        return self.nanSeries()


movingAverage('dataset','period').yazdir

    
      


