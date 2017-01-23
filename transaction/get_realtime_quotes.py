import tushare as ts

df = ts.get_realtime_quotes('600036') #Single stock symbol
# print df[['code','name','price','bid','ask','volume','amount','time']]
print df


#      code  name   price     bid     ask    volume         amount      time
# 0  600036  招商银行  18.590  18.570  18.580  21739051  403155082.000  15:00:00