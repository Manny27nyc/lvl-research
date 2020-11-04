import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style as style
from datetime import datetime
import json

# import data
to_dt = lambda x : datetime.utcfromtimestamp(x)
with open("data/volume-btc.json", "r") as f:
	pl = json.loads(f.read())
	pl["values"]
	x_btc, y_btc = zip(*[(to_dt(d['x']), d['y']) for d in pl["values"]])
with open("data/volume-usd.json", "r") as f:
	pl = json.loads(f.read())
	pl["values"]
	x_usd, y_usd = zip(*[(to_dt(d['x']), d['y']) for d in pl["values"]])

# analysis
lmbda = 0.95
weights = [lmbda ** i for i in range(15)]
weights = [w / sum(weights) for w in weights]
ma = lambda x : np.convolve(x, weights, 'same')
y_btc_avg = ma(y_btc)
y_usd_avg = ma(y_usd)

style.use('fivethirtyeight')
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.rcParams['lines.linewidth'] = 2

# print(plt.rcParams.keys() )
# plot data
plt.plot(x_btc, y_btc, c='b', alpha=0.2, label='Data')
plt.plot(x_btc, y_btc_avg, c='b', alpha=1.0, label='Moving Average')
plt.ylabel('BTC Transaction Volume (BTC)')
plt.xlabel('Time')
plt.yticks([0, 1E6, 2E6, 3E6, 4E6, 5E6, 6E6], ['0  ', '1  ', '2  ', '3  ', '4  ', '5  ', '6M ']) 
plt.legend()
plt.show()

plt.plot(x_usd, y_usd, c='b', alpha=0.2, label='Data')
plt.plot(x_usd, y_usd_avg, c='b', alpha=1.0, label='Moving Average')
plt.ylabel('BTC Transaction Volume (USD)')
plt.xlabel('Time')
plt.yticks([0, 1E9, 2E9, 3E9, 4E9, 5E9, 6E9], ['0  ', '1  ', '2  ', '3  ', '4  ', '5  ', '6M ']) 
plt.legend()
plt.show()