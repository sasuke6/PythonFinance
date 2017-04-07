from sqlalchemy import create_engine

import tushare as ts

df = ts.get_tick_data('600036', date='2017-04-05')

engine = create_engine('mysql://root@127.0.0.1/stock?charset=utf8')

df.to_sql('tick_data', engine)

