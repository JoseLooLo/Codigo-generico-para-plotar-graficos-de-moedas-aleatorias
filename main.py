from plot import Plot
from graph import Graph

dictMA = []
dictCS = []

#Gráficos duplicados pela limitação da quantidade de requests da api

plot2 = Plot( "BTC", "CNY", "AAAAAA", 100)
temp = plot2.getInfoRequestMA()
temp2 = plot2.getInfoRequestCandlestick()
dictCS.append(temp2)
dictCS.append(temp2)
dictMA.append(temp)
dictMA.append(temp)


plot3 = Plot( "EOS", "CNY", "tisctisc", 100)
temp = plot3.getInfoRequestMA()
temp2 = plot3.getInfoRequestCandlestick()
dictCS.append(temp2)
dictCS.append(temp2)
dictMA.append(temp)
dictMA.append(temp)

graph = Graph(dictCS, dictMA)
graph.graph_all()