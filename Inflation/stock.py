from sqlalchemy import create_engine

import tushare as ts

df = ts.get_industry_classified()

for index, code in enumerate(df.code):
    if index > 1000 and index <= 1500:
        dd = ts.get_k_data(code, ktype='M')

        engine = create_engine('mysql://root@127.0.0.1/stock?charset=utf8')

        dd.to_sql(code, engine, if_exists='replace', index=False,chunksize=200)


# ds.to_sql('Test', engine, if_exists='append', index=False)

