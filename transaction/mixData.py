import tushare as ts
import pandas as pd 
import matplotlib.pyplot

fig = matplotlib.pyplot.gcf()


df = ts.get_today_ticks('600036')
ds = df.sort_index()
dd =  ds.head(10)
with pd.plot_params.use('x_compat', True):
    dd.price.plot(color='g',figsize=(10,4),grid='on')
    # dd.time.plot(color='y',figsize=(10,4),grid='on')
    # dd.high.plot(color='r',figsize=(10,4),grid='on')
    # dd.low.plot(color='b',figsize=(10,4),grid='on')
    fig.savefig('graph2.png')