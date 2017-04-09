from sqlalchemy import create_engine

import tushare as ts

from pandas import DataFrame

df = ts.get_industry_classified()

# engine = create_engine('mysql://root@127.0.0.1/stock?charset=utf8')

# df.to_sql('industry', engine)

for code in df.code:
    ds = DataFrame({
        'code' : [code],
    })

    print ds
    break

# tmp = df.code[0]

# print tmp
