import tushare as ts
df = ts.get_hist_data('600848', start='2017-01-05', end='2017-01-09')
print df







#              open   high  close    low    volume  price_change  p_change  \
# date
# 2017-01-09  20.38  20.56  20.40  19.75  54709.33          0.21      1.04
# 2017-01-06  20.00  20.50  20.19  19.97  77353.22          0.13      0.65
# 2017-01-05  19.78  20.40  20.06  19.47  76149.86          0.29      1.47

#               ma5    ma10    ma20     v_ma5    v_ma10    v_ma20  turnover
# date
# 2017-01-09  19.98  19.790  19.305  55945.29  55870.80  65193.66      1.37
# 2017-01-06  19.77  19.734  19.255  56334.87  59176.11  68468.46      1.94
# 2017-01-05  19.70  19.757  19.291  55831.08  66487.87  66605.56      1.91