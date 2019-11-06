import matplotlib.pyplot as plt
import mpl_finance
import numpy as np

class Graph:

    def __init__(self, dictCS, dictMA):
        self.dictCS = dictCS
        self.dictMA = dictMA

    def Candlestick(self):
        figure, axe = plt.subplots(figsize = (8,5))
        quotes = []
        for index in range(len(self.dictCS["datas"])):
            quotes.append(tuple ([self.dictCS["datas"][index], self.dictCS["open"][index], self.dictCS["high"][index], self.dictCS["low"][index], self.dictCS["close"][index],]))
        mpl_finance.candlestick_ohlc(axe, quotes, colordown='r', colorup='g')
        axe.xaxis_date()
        plt.xticks(rotation=20)
        plt.title("Simple Plot")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.show()

    def MediaMovel(self):
        figure, axe = plt.subplots(figsize = (8,5))
        axe.plot(self.dictMA["datas"], self.dictMA["media"], 'r--', alpha=0.75, label = "Média Móvel")
        axe.plot(self.dictCS["datas"], self.dictCS["open"], 'b--', alpha=0.75, label = "Open")
        axe.xaxis_date()
        plt.xticks(rotation=20)
        plt.title("Simple Plot")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

    def Volume(self):
        figure, axe = plt.subplots(figsize = (8,5))
        axe.plot(self.dictCS["datas"], self.dictCS["volume"], 'b', alpha=0.5, label = "Volume")
        axe.xaxis_date()
        plt.xticks(rotation=20)
        plt.title("Simple Plot")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

    def graph_all(self):
        figure, axe1 = plt.subplots(figsize = (10,5))
        quotes = []
        for index in range(len(self.dictCS["datas"])):
            quotes.append(tuple ([self.dictCS["datas"][index], self.dictCS["open"][index], self.dictCS["high"][index], self.dictCS["low"][index], self.dictCS["close"][index],]))
        mpl_finance.candlestick_ohlc(axe1, quotes, colordown='r', colorup='g')
        axe1.plot(self.dictMA["datas"], self.dictMA["media"], 'r--', alpha=0.75, label = "Média Móvel")
        axe1.plot(self.dictCS["datas"], self.dictCS["volume"], 'b', alpha=0.5, label = "Volume")
        axe1.margins(x=0, y=-0.25) #Zoom
        axe1.xaxis_date()
        plt.xticks(rotation=20)
        plt.title("Simple Plot")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()