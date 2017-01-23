import tushare as ts

df = ts.get_hist_data('600036')

df.to_csv('600036.csv')
