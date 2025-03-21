import yfinance as yf
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc

start_date = '2023-01-01'
end_date = '2023-10-01'
plt.figure(figsize=(12,6))

btc_data = yf.download('BTC-USD', start=start_date, end=end_date)

print(btc_data.columns)

btc_data = btc_data[[('Open','BTC-USD'),('High','BTC-USD'),('Low','BTC-USD'),('Close','BTC-USD')]]
btc_data.reset_index(inplace=True)
btc_data['Date'] = btc_data['Date'].map(mdates.date2num)
print(btc_data.tail())

ax = plt.subplot()
ax.xaxis_date()

candlestick_ohlc(ax, btc_data.values)

plt.show()
