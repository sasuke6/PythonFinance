from sqlalchemy import create_engine

from pandas import DataFrame

import tushare as ts

# df = ts.get_k_data('600036', start='2017-04-05', end='2017-04-07')

# print df.T

# dfT = df.T

# tmp = dfT.drop(['open','high','low', 'volume','code'])

# tmp = df[['date','close']]
# tmp.index = ['2017-04-05', '2017-04-06', '2017-04-07']
# print tmp

engine = create_engine('mysql://root@127.0.0.1/stock?charset=utf8')


ds = DataFrame({
    'age' : [24,25,26],
    'name': ['XU' , 'ZHI', 'YONG']
})

ds['height'] = 178

print ds

# ds.to_sql('ds_data', engine, if_exists='append', index=False)

