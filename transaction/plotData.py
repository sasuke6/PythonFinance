import tushare as ts
import pandas as pd 
import matplotlib.pyplot

fig = matplotlib.pyplot.gcf()


df = ts.get_hist_data('600036', start='2017-01-05', end='2017-01-24')
ds = df.sort_index()
with pd.plot_params.use('x_compat', True):
    ds.open.plot(color='g',figsize=(10,4),grid='on')
    ds.close.plot(color='y',figsize=(10,4),grid='on')
    ds.high.plot(color='r',figsize=(10,4),grid='on')
    ds.low.plot(color='b',figsize=(10,4),grid='on')
    fig.savefig('graph1.png')