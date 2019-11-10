import matplotlib.pyplot as plt
import mpl_finance
import numpy as np

class Graph:

    def __init__(self, dictCS, dictMA):
        self.dictCS = dictCS
        self.dictMA = dictMA

    def graph_all(self):
        figure, axe = plt.subplots(2,2)

        k = 0
        for i in range(2):
            for j in range(2):
                quotes = []
                for index in range(len(self.dictCS[k]["datas"])):
                    quotes.append(tuple ([self.dictCS[k]["datas"][index], self.dictCS[k]["open"][index], self.dictCS[k]["high"][index], self.dictCS[k]["low"][index], self.dictCS[k]["close"][index],]))
                mpl_finance.candlestick_ohlc(axe[i][j], quotes, colordown='r', colorup='g')
                axe[i][j].plot(self.dictMA[k]["datas"], self.dictMA[k]["media"], 'r--', alpha=0.75)
                #axe[i][j].bar(self.dictCS[k]["datas"], self.dictCS[k]["volume"])
                #axe[i][j].margins(x=0, y=-0.25) #Zoom
                axe[i][j].xaxis_date()
                for tick in axe[i,j].get_xticklabels():
                    tick.set_rotation(20)
                for tick in axe[j,i].get_xticklabels():
                    tick.set_rotation(20)
                k+=1

        for ax in axe.flat:
            ax.label_outer()

        plt.show()