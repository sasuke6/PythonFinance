import tushare as ts
df = ts.get_k_data('600848', start='2017-01-05', end='2017-01-09')
print df




#          date   open  close   high    low   volume    code
# 2  2017-01-05  19.78  20.06  20.40  19.47  76149.0  600848
# 3  2017-01-06  20.00  20.19  20.50  19.97  77353.0  600848
# 4  2017-01-09  20.38  20.40  20.56  19.75  54709.0  600848