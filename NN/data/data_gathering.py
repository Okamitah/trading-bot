import yfinance as yf
import matplotlib
matplotlib.use('TkAgg') # Because I use Vim, I need this module
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick_ohlc

start_date = '2014-01-03'
end_date = '2025-03-23'
plt.figure(figsize=(12,6))

btc_data = yf.download('BTC-USD', start=start_date, end=end_date)
btc_data.to_csv('data/btc.csv')
eth_data = yf.download('ETH-USD', start=start_date, end=end_date)
btc_data.to_csv('data/eth.csv')
sol_data = yf.download('SOL-USD', start=start_date, end=end_date)
btc_data.to_csv('data/sol.csv')
bnb_data = yf.download('BNB-USD', start=start_date, end=end_date)
btc_data.to_csv('data/bnb.csv')

print(f"Type: {type(bnb_data)}")

btc_data = btc_data[
                [('Open','BTC-USD'),('High','BTC-USD'),
                 ('Low','BTC-USD'),('Close','BTC-USD')]
            ]

eth_data = eth_data[
                [('Open','ETH-USD'),('High','ETH-USD'),
                 ('Low','ETH-USD'),('Close','ETH-USD')]
            ]

sol_data = sol_data[
                [('Open','SOL-USD'),('High','SOL-USD'),
                 ('Low','SOL-USD'),('Close','SOL-USD')]
            ]

bnb_data = bnb_data[
                [('Open','BNB-USD'),('High','BNB-USD'),
                 ('Low','BNB-USD'),('Close','BNB-USD')]
            ]

btc_data.reset_index(inplace=True)
eth_data.reset_index(inplace=True)
print(btc_data['Date'][0])
btc_data['Date'] = btc_data['Date'].map(mdates.date2num)
eth_data['Date'] = eth_data['Date'].map(mdates.date2num)
print(btc_data.head())
print(eth_data.head())

ax = plt.subplot()
ax.xaxis_date()

candlestick_ohlc(ax, eth_data.values)

plt.show()
