import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as pyo
from datetime import datetime
import trade
import  showplots

def MACD (EMA12 , EMA26):
    MACDR = np.zeros_like(EMA12)
    for i in range(len(EMA12)):
        MACDR[i] = EMA12[i] - EMA26[i]
    return MACDR

def EMA(arr, n):
    k = 2 / (n + 1)
    ema = np.zeros_like(arr)
    #ADD  FIRST ELEMENT TO EMA
    for i in range(0 ,n):
        ema[i] = arr[i]
    for value in range(n ,len(arr)):
        licznik = arr[value]
        denominator = 1
        for i in range(1, n):
            denominator += (1 - k)**i # mianownik
            if value - i >= 0:
                licznik += arr[value - i] * (1 - k)**i # licznik
        ema[value] = licznik/denominator
    return ema






# def printresult(df, easyplayer, mediumplayer, riskplayer):
#     plt.plot(df['Date'],easyplayer.numberofShares, label='Signal')
#     plt.plot(df['Date'],mediumplayer.numberofShares, label='MACD')
#     plt.plot(df['Date'],riskplayer.numberofShares, label='MACD')
#     plt.xticks(df['Date'][::500])
#     plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_csv('AMD.csv')

    orginaldata = df["Close"].tolist()
    EMA12 = EMA(orginaldata, 12)
    EMA26 = EMA(orginaldata, 26)
    EMA100 = EMA(orginaldata, 100)
    MACD = MACD(EMA12, EMA26)
    #print_MACD(df, MACD)
    #print_MACDInteractive(df, MACD)
    #print_plot(df, EMA12, EMA26, EMA100)
    #print_plotflex(df, EMA12, EMA26, EMA100)

    easyplayer = trade.Person(1000, 2, 0.95)
    mediumplayer = trade.Person(1000, 4, 0.95)
    riskplayer = trade.Person(1000, 8, 0.95)
    moneyvalueation = []
    for x in range(len(MACD)):
        easyplayer.shouldbuy(MACD[x], orginaldata[x])
        moneyvalueation.append(easyplayer.numberofShares*orginaldata[x])
        # print(easyplayer.numberofShares)
        # print(easyplayer.money)
        # print(easyplayer.moneytable)
        #mediumplayer.shouldbuy(MACD[x], orginaldata[x])
        #riskplayer.shouldbuy(MACD[x], orginaldata[x])
    for x in range(len(MACD)):
        easyplayer.sell(easyplayer.numberofShares, orginaldata[-1])
    print(easyplayer.numberofShares)
    print(easyplayer.money)
    print(easyplayer.moneytable)

    showplots.test(moneyvalueation, easyplayer.moneytable, df)
    #printresult(df, easyplayer, mediumplayer, riskplayer)
