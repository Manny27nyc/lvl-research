import numpy as np
from matplotlib import pyplot as plt
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

# plot data
plt.plot(x_btc, y_btc, c='b', alpha=0.2)
plt.plot(x_btc, y_btc_avg, c='b', alpha=1.0)
plt.ylabel('BTC Transaction Volume (BTC)')
plt.xlabel('Time')
plt.show()

plt.plot(x_usd, y_usd, c='b', alpha=0.2)
plt.plot(x_usd, y_usd_avg, c='b', alpha=1.0)
plt.ylabel('BTC Transaction Volume (USD)')
plt.xlabel('Time')
plt.show()