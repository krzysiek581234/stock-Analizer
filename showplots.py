from matplotlib import pyplot as plt
import plotly.graph_objs as go

from main import EMA


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

def test(moneyvalueation, moneytable, df):
    dates = df['Date']

    # stworzenie figury i osi x
    fig, ax = plt.subplots()
    ax.set_xlabel('Days')



    ax.plot(moneyvalueation, label='moneyvalueation', color='blue')
    ax.set_ylabel('Money Valueation', color='blue')
    ax.set_ylim([0, 4000])

    ax2 = ax.twinx()
    ax2.plot(moneytable, label='moneytable', color='red')
    ax2.spines['right'].set_position(('axes', 1))
    ax2.set_ylabel('Cash left', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim([0, 1500])
    plt.show()







