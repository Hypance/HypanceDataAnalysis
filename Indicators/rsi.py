import pandas as pd
rsi_db = pd.read_excel("/Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/rsidosyasi.xlsx")
data_close = rsi_db["close"]
class Rsi_counter():

    def __int__(self, data_close, total_gain, total_loss):
        self.data_close = data_close
        self.total_loss = total_loss
        self.total_gain = total_gain


    def gain_calculator(self):
        total_gain = 0
        for i in range(0, 14):
            if data_close[i+1] > data_close[i]:
                gain = (data_close[i+1] - data_close[i])
                total_gain = total_gain + gain
        return total_gain


    def loss_calculator(self):
        total_loss = 0
        for i in range(0, 14):
            if data_close[i] > data_close[i+1]:
                loss = data_close[i] - data_close[i+1]
                total_loss = total_loss + loss
        return total_loss

    def rsi_function(self):
        total_gain = self.gain_calculator()
        total_loss =self.loss_calculator()
        rs = total_gain/total_loss
        rsi = 100 - (100/(1+rs))
        return rsi


Result = Rsi_counter()
print(Result.rsi_function())
