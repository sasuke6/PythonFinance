from sqlalchemy import create_engine

import tushare as ts

df = ts.get_hs300s()

engine = create_engine('mysql://root@127.0.0.1/stock?charset=utf8')

for code in df.code:
    dd = ts.get_k_data(code, ktype='M')

    dd.to_sql(code, engine, if_exists='replace', chunksize=100)



# df.to_sql('ShangShen', engine, if_exists='replace', chunksize=100)