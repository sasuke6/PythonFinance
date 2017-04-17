#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from sqlalchemy import create_engine
from pandas import DataFrame

db = MySQLdb.connect("127.0.0.1", "root", "", "stock", charset='utf8')

cursorCode = db.cursor()
cursorMax = db.cursor()
cursorMin = db.cursor()

# sqlMax = "select max(`close`) from `000001` where date>'2008-12-31' and date<'2015-12-31'"
# sqlMin = "select min(`close`) from `000001` where date>'2008-12-31' and date<'2015-12-31'"
sqlCode = "select code, name from `ShangShen`"

# test = "select max(`close`) from " + "ShangShen" + " where date>'2008-12-31' and date<'2015-12-31'"
engine = create_engine('mysql://root@127.0.0.1/stock?charset=utf8')

cursorCode.execute(sqlCode)
result = cursorCode.fetchall()
for row in result:
    code = row[0]
    name = row[1]
    sqlMax = "select max(`close`) from `%s` " % code + "where date>'2008-12-31' and date<'2015-12-31'"
    sqlMin = "select min(`close`) from `%s` " % code + " where date>'2008-12-31' and date<'2015-12-31'"
    cursorMax.execute(sqlMax)
    cursorMin.execute(sqlMin)
    resultMax = cursorMax.fetchone()[0]
    resultMin = cursorMin.fetchone()[0]
    if resultMax < 0 and resultMin < 0:
        continue
    data = (resultMax / resultMin) * 100
    ds = DataFrame({
        'code' : [code],
        'name' : [name],
        'resultMin' : [resultMin],
        'resultMax' : [resultMax],
        'percent' : [data]
    })
    # print code, name, resultMin, resultMax ,data
    ds.to_sql('Desc', engine, if_exists='append', index=False)

# try:
#     cursorCode.excute(sqlCode)
#     result = cursorCode.fetchall()
#     for row in result:
#         code = row[0]
#         name = row[1]
#         sqlMax = "select max(`close`) from " + code + " where date>'2008-12-31' and date<'2015-12-31'"
#         sqlMin = "select min(`close`) from " + code + " where date>'2008-12-31' and date<'2015-12-31'"
#         print sqlMax, sqlMin
#         cursorMax.execute(sqlMax)
#         cursorMin.execute(sqlMin)
#         resultMax = cursor.fetchone()[0]
#         resultMin = cursor2.fetchone()[0]
#         data = (resultMax / resultMin) * 100
#         print code, name, data
# except :
#     print "Error: unable to fecth data"

db.close()