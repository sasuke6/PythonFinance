import tushare as ts
df = ts.get_k_data('399300', index=True,start='2016-10-01', end='2016-10-31');
print df



#            date     open    close     high      low       volume      code
# 184  2016-10-10  3265.36  3293.87  3294.64  3258.96   80519260.0  sz399300
# 185  2016-10-11  3296.87  3306.56  3308.00  3292.88   87713163.0  sz399300
# 186  2016-10-12  3299.14  3300.01  3302.56  3289.75   68669781.0  sz399300
# 187  2016-10-13  3299.16  3302.65  3307.41  3292.40   81224198.0  sz399300
# 188  2016-10-14  3298.73  3305.85  3306.69  3285.73   82316271.0  sz399300
# 189  2016-10-17  3305.96  3277.88  3309.01  3271.54   86113509.0  sz399300
# 190  2016-10-18  3272.68  3321.33  3321.33  3272.68  102860714.0  sz399300
# 191  2016-10-19  3323.30  3316.24  3332.52  3309.83  101167725.0  sz399300
# 192  2016-10-20  3317.18  3318.60  3324.90  3312.17   79238871.0  sz399300
# 193  2016-10-21  3315.72  3327.74  3341.56  3309.18  109785176.0  sz399300
# 194  2016-10-24  3332.51  3367.58  3382.83  3330.97  153014345.0  sz399300
# 195  2016-10-25  3367.48  3367.45  3373.91  3356.59  111191693.0  sz399300
# 196  2016-10-26  3365.20  3354.80  3367.83  3349.57   98024786.0  sz399300
# 197  2016-10-27  3351.46  3345.70  3352.35  3335.13   77629851.0  sz399300
# 198  2016-10-28  3347.14  3340.13  3370.75  3337.29   93133309.0  sz399300
# 199  2016-10-31  3332.41  3336.28  3340.47  3317.33   71352863.0  sz399300