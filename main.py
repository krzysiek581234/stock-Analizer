import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as pyo
from datetime import datetime
import trade

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

def print_plot(df, EMA12, EMA26, EMA100):
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Close'], label='normal')
    plt.xticks(df['Date'][::500])
    ax.plot(EMA12, label='EMA12')
    ax.plot(EMA26, label='EMA26')
    ax.plot(EMA100, label='EMA100')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.legend(loc='upper left')
    ax.set_title('AMD close Prices')
    plt.show()

import plotly.graph_objects as go

def print_plotflex(df, EMA12, EMA26, EMA100):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='normal'))
    fig.add_trace(go.Scatter(x=df['Date'], y=EMA12, name='EMA12'))
    fig.add_trace(go.Scatter(x=df['Date'], y=EMA26, name='EMA26'))
    fig.add_trace(go.Scatter(x=df['Date'], y=EMA100, name='EMA100'))
    fig.update_layout(title='AMD close Prices', xaxis_title='Date', yaxis_title='Price')
    fig.show()


def print_MACD(df, MACD):
    SIGNAL = EMA(MACD, 9)
    plt.plot(df['Date'],SIGNAL, label='Signal')
    plt.plot(df['Date'],MACD, label='MACD')
    plt.xticks(df['Date'][::500])
    plt.show()


def print_MACDInteractive(df, MACD):
    SIGNAL = EMA(MACD, 9)
    trace1 = go.Scatter(x=df['Date'], y=SIGNAL, mode='lines', name='Signal')
    trace2 = go.Scatter(x=df['Date'], y=MACD, mode='lines', name='MACD')
    data = [trace1, trace2]
    layout = go.Layout(title='MACD', xaxis={'title': 'Data'}, yaxis={'title': 'Wartość'})
    fig = go.Figure(data=data, layout=layout)
    fig.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_csv('AMD.csv')

    orginaldata = df["Close"].tolist()
    EMA12 = EMA(orginaldata, 12)
    EMA26 = EMA(orginaldata, 26)
    EMA100 = EMA(orginaldata, 100)
    MACD = MACD(EMA12, EMA26)
    print_MACD(df, MACD)
    print_MACDInteractive(df, MACD)
    print_plot(df, EMA12, EMA26, EMA100)
    print_plotflex(df, EMA12, EMA26, EMA100)

    easyplayer = trade.Person(1000, 0.25, 0.95)
    mediumplayer = trade.Person(1000, 0.5, 0.95)
    riskplayer = trade.Person(1000, 7.5, 0.95)

    for x in range(len(MACD)):
        easyplayer.shouldbuy(MACD[x], orginaldata[x])
        mediumplayer.shouldbuy(MACD[x], orginaldata[x])
        riskplayer.shouldbuy(MACD[x], orginaldata[x])