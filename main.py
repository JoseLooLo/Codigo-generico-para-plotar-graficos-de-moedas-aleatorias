from plot import Plot
from graph import Graph

plot = Plot( "BTC", "CNY", 100)
dictMA = plot.getInfoRequestMA()
dictCS = plot.getInfoRequestCandlestick()
graph = Graph(dictCS, dictMA)
graph.graph_all()