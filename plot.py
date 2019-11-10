import matplotlib.dates as mdates
from datetime import date
import requests

class Plot:

    base_url = "https://www.alphavantage.co/query?"
    #api_key = "UmaKeyGenerica"

    def __init__(self, symbol, market, key, days = 0):
        self.symbol = symbol
        self.market = market
        self.days = days
        self.api_key = key

    def getInfoRequestCandlestick(self):
        function = "DIGITAL_CURRENCY_DAILY"
        url = f"{self.base_url}function={function}&symbol={self.symbol}&market={self.market}&apikey={self.api_key}"
        print(url)
        response = requests.get(url)
        response = response.json()

        datas = []
        if self.days == 0:
            datas = [index for index, value in response['Time Series (Digital Currency Daily)'].items()]
        else:
            count = 0
            for index, value in response['Time Series (Digital Currency Daily)'].items():
                datas.append(index)
                count +=1
                if count > self.days:
                    break

        get_open =   [int(float(response['Time Series (Digital Currency Daily)'][data][f"1a. open ({self.market})"])) for data in datas]
        get_high =   [int(float(response['Time Series (Digital Currency Daily)'][data][f"2a. high ({self.market})"])) for data in datas]
        get_low =    [int(float(response['Time Series (Digital Currency Daily)'][data][f"3a. low ({self.market})"])) for data in datas]
        get_close =  [int(float(response['Time Series (Digital Currency Daily)'][data][f"4a. close ({self.market})"])) for data in datas]
        get_volume = [int(float(response['Time Series (Digital Currency Daily)'][data][f"5. volume"])) for data in datas]
        #get_cap =    [int(float(response['Time Series (Digital Currency Daily)'][data][f"6. market cap (USD)"])) for data in datas]
        datas_floatValue = [mdates.date2num(date(int(data[0:4]), int(data[5:7]), int(data[8:10]))) for data in datas]

        return {
            "datas" : datas_floatValue,
            "open"  : get_open,
            "high"  : get_high,
            "low"   : get_low,
            "close" : get_close,
            "volume": get_volume
            #"cap"   : get_cap
        }

    def getInfoCSVCandlestick(self):
        pass
    
    def getInfoRequestMA(self):
        function = "SMA"
        interval = "daily"
        time_period = "30"
        series_type = "open"
        url = f"{self.base_url}function={function}&symbol={self.symbol}{self.market}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={self.api_key}"
        print(url)
        response = requests.get(url)
        response = response.json()

        datas = []
        if self.days == 0:
            datas = [index for index, value in response['Technical Analysis: SMA'].items()]
        else:
            count = 0
            for index, value in response['Technical Analysis: SMA'].items():
                datas.append(index)
                count +=1
                if count > self.days:
                    break

        get_ma = [int(float(response['Technical Analysis: SMA'][data]["SMA"])) for data in datas]
        datas_floatValue = [mdates.date2num(date(int(data[0:4]), int(data[5:7]), int(data[8:10]))) for data in datas]

        return {
            "datas" : datas_floatValue,
            "media"   : get_ma
        }
