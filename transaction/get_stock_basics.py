import tushare as ts
df = ts.get_stock_basics()
date = df.ix['600848']['timeToMarket']
print date


# 19940324a