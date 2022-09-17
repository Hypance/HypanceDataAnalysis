from cmath import nan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def moving_average(a,n):              # n değeri yerine girilen sayılık günlük ortalama bulduruyor
    ret = np.cumsum(a,dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n-1:] / n

def plotMA(dataframe,series,df1): #İstenilen grafik tablosunu çizdiriyor
    print(df1)
    dataframe.plot()
    series.plot()
    plt.show()

def nanSeries(Serie,i):
    nanSeri=[]
    for _ in range(i):
        nanSeri.append(nan) #istediğimiz vakitten itibaren ortalamanın plot için gerekli boşlukları sağlayacak
    nanSeri[(2*i+2):] = Serie
    return nanSeri




data = pd.read_excel('movingaverage.xlsx')
sales = data['Sales']
dates = data['Date']


arrMoving3=pd.Series(moving_average(np.array(sales),3))
arrMoving5=pd.Series(moving_average(np.array(sales),5))
arrMoving7=pd.Series(moving_average(np.array(sales),7))
finalSeries3 = pd.Series(nanSeries(arrMoving3,3))  #3 günlük hareketli ortalama
finalSeries5 = pd.Series(nanSeries(arrMoving5,5))  #5 günlük hareketli ortalama
finalSeries7 = pd.Series(nanSeries(arrMoving7,7))  #7 günlük hareketli ortalama

df1=pd.DataFrame(finalSeries3) 
df1.columns = ['3-Days']
df1['5-Day'] = finalSeries5
df1['7-Day'] = finalSeries7
plotMA(sales,finalSeries5,df1)

