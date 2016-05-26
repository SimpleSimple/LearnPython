# -*- coding: utf-8 -*-

# 测试添加数据到mysql

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='testdb', charset='utf8')
cur=conn.cursor()

cur.execute("INSERT INTO tb_position(positionname) VALUES('Python工程师')")

cur.close()
conn.close()

###################################
#
#   1.将数据插入到mysql的时候表名不要使用保留关键字, position为mysql保留关键字
#   2.mysql创建数据库的时候需要设置字符集为utf-8，不要用默认的latin-1，否则数据录入到数据库会乱码
#
###################################