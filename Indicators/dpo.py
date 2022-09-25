import numpy as np 

class DPO:
    def __init__(self,arr:list,period:int=4) -> None: #gereken inputlar: dataset(array),period(int)
        self.arr = arr
        self.period = period

    def moving_average(self):              # self.period değeri yerine girilen sayılık günlük ortalama bulduruyor
        n = self.period
        ret = np.cumsum(self.arr)
        ret[n:] = ret[n:] - ret[:-n]
        return ret[n-1:] / n
    
    def closes(self): #bize gereken (n/2)+1. kapanış değerini alacak ve bunu bir liste haline getirecek fonksiyon
        n = self.period
        tempArr = []
        for i in range(n-2,((n-2)+2*len(self.moving_average())),2):
            tempArr.append(self.arr[(i//2)+1])
        periodCloses = np.array(tempArr)
        return periodCloses

    def yazdir(self): #liste döndürecek yazdirma fonksiyonu, bu çağırılacak.
        dpoFinalize = np.subtract(self.closes(),self.moving_average())
        return dpoFinalize