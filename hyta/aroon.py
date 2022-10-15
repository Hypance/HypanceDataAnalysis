import pandas as pd
import openpyxl
import numpy as np
import xlrd

class Aroon():

    def __init__(self, first_day = 0, last_day = 26):
        self.first_day = first_day
        self.last_day = last_day
        self.period = self.last_day - self.first_day + 1

    def high_finder(self):
        data = high_data.iloc[self.first_day : self.last_day + 1].tolist()
        print(data.index(max(data)))
        return self.period - data.index(max(data)) + 1

    def low_finder(self):
        data = low_data.iloc[self.first_day: self.last_day + 1].tolist()
        print(data.index(min(data)))
        print(self.period - data.index(min(data)) + 1)
        print(self.period)
        return self.period - data.index(min(data)) + 1

    def aroon_up(self) -> float:
        aroon_up = (((self.period - self.high_finder()) / 2) / self.period) * 100
        return aroon_up

    def aroon_down(self) -> float:
        aroon_down = (((self.period - self.low_finder()) / 2) / self.period) * 100
        return aroon_down

    def aroon_oscilattor(self):
        return self.aroon_up - self.aroon_down()

datas = pd.read_excel("/Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/Aroon.Oscillator.xls")
high_data = (datas["High"])
low_data = (datas["Low"])

result = Aroon()
print(result.low_finder())