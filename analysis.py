import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style as style
from datetime import datetime
from matplotlib import ticker
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

# print(plt.rcParams.keys() )
# plot data
plt.figure(1)
fig = plt.gcf()
ax = plt.gca()
fig.set_size_inches(6.4, 4.8)
plt.subplots_adjust(left=0.1, bottom=0.13, right=0.95, top=0.9)
plt.autoscale(enable=True, axis='x', tight=True)
ax.set_facecolor("#f9f9f9")
fig.patch.set_facecolor("#f9f9f9")
plt.plot(x_btc, y_btc, c='b', alpha=0.2, label='Data')
plt.plot(x_btc, y_btc_avg, c='b', alpha=1.0, label='Moving Average')
plt.title("BTC Transaction Volume")
plt.ylabel('BTC (millions)')
plt.xlabel('Time')
ax.yaxis.set_major_formatter(
	lambda x, pos : "{:.0f}".format(x / 1e6)
)
plt.legend()
fig.savefig('renders/btc_tv.png', dpi=100)

plt.figure(2)
fig = plt.gcf()
ax = plt.gca()
fig.set_size_inches(6.4, 4.8)
plt.subplots_adjust(left=0.1, bottom=0.13, right=0.95, top=0.9)
plt.autoscale(enable=True, axis='x', tight=True)
plt.autoscale(enable=True, axis='x', tight=True)
ax.set_facecolor("#f9f9f9")
fig.patch.set_facecolor("#f9f9f9")
plt.plot(x_usd, y_usd, c='b', alpha=0.2, label='Data')
plt.plot(x_usd, y_usd_avg, c='b', alpha=1.0, label='Moving Average')
plt.title("BTC Transaction Volume (USD)")
plt.ylabel('USD (billions)')
plt.xlabel('Time')
ax.yaxis.set_major_formatter(
	lambda x, pos : "{:.0f}".format(x / 1e9)
)
plt.legend()
fig.savefig('renders/btc_tv_usd.png', dpi=100)

plt.show()