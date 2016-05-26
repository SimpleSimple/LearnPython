# -*- coding: utf-8 -*-

import requests
import re
import json
import pymysql
import string

#python 3.x 已不能使用MySQLdb了
# import MySQLdb

# import pandas as pd

# # 匿名函数
# def calc_sum(x):
#     return x*x
#
# def now():
#     print('2016-1-30')
#
# x = nowe
# x()
#
# print(now.__name__)
# print(now().__name__)

#调用github时间线json，返回json数据
# r=requests.get('https://www.github.com/timeline.json', timeout=6)
# print(r.json())
# print('Print Json Message:')
# print(r.json()['documentation_url'])

print('aaabbders\n\ndfsdf'.replace("\n"," "))

r = requests.get('https://www.zhihu.com/question/30116337')

# pattern=re.compile('zh-question-title.+?<h2.+?>(.+?)</h2>')
# m2=re.search(pattern, strtext)
# print(m2)

# print('\u2256'.encode('gbk', 'ignore'))



# # 检查类型
# jsondata = json.loads(str('[{"createTime":"2016-05-05 16:34:53","companyId":122145,"adjustScore":0,"positionName":"网络推广","companyName":"高浪灯光","education":"大专","city":"广州","positionType":"运营","positionId":1650973,"financeStage":"成熟型(D轮及以上)","companyShortName":"广州高浪电子科技有限公司","companyLogo":"i/image/M00/1A/86/Cgp3O1b6RNOAAdIyAAC6NKvPmTQ858.jpg","salary":"6k-8k","industryField":"电子商务","deliverCount":0,"positionAdvantage":"7小时工作时，不用外出，包吃住","companyLabelList":[],"jobNature":"全职","workYear":"1-3年","positionFirstType":"运营","score":0,"leaderName":"暂没有填写","companySize":"50-150人","formatCreateTime":"16:34发布","calcScore":false,"orderBy":66,"showOrder":0,"haveDeliver":false,"adWord":0,"randomScore":0,"countAdjusted":false,"relScore":0,"imstate":"disabled","createTimeSort":1462437293000,"positonTypesMap":null,"hrScore":17,"flowScore":0,"showCount":31,"pvScore":7.536407063294263,"plus":"否","totalCount":0,"searchScore":0.0},{"createTime":"2016-05-05 16:34:51","companyId":122145,"adjustScore":0,"positionName":"外贸业务员（舞台灯光）","companyName":"高浪灯光","education":"学历不限","city":"广州","positionType":"销售","positionId":1700305,"financeStage":"成熟型(D轮及以上)","companyShortName":"广州高浪电子科技有限公司","companyLogo":"i/image/M00/1A/86/Cgp3O1b6RNOAAdIyAAC6NKvPmTQ858.jpg","salary":"3k-6k","industryField":"电子商务","deliverCount":0,"positionAdvantage":"朝九晚五，包食宿，购买社保，出国机会","companyLabelList":[],"jobNature":"全职","workYear":"1-3年","positionFirstType":"市场与销售","score":0,"leaderName":"暂没有填写","companySize":"50-150人","formatCreateTime":"16:34发布","calcScore":false,"orderBy":66,"showOrder":0,"haveDeliver":false,"adWord":0,"randomScore":0,"countAdjusted":false,"relScore":0,"imstate":"disabled","createTimeSort":1462437291000,"positonTypesMap":null,"hrScore":17,"flowScore":0,"showCount":70,"pvScore":15.04733474733546,"plus":"否","totalCount":0,"searchScore":0.0}]'))
#
# data = {}
# data['positionName']=''
# data['companyShortName']=''
# data['city']=''
#
# for i in range(len(jsondata)):
#     data['positionName']=jsondata[i]['positionName']
#     data['companyShortName']=jsondata[i]['companyShortName']
#     data['city']=jsondata[i]['city']
#
#     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='testdb', charset='utf8')
#     cur = conn.cursor()
#     cur.execute("INSERT INTO tb_position(positionname) values('"+data['positionName']+"')")
#
#     cur.close()
#     conn.close()
#     # 1.0 使用的MySQLdb库插入mysql数据，只能python 2.x下用
#     # conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='', db='test')
#     # cur=conn.cursor()
#     #
#     # sql="insert into postition(positionName, companyShortName, city) values(%s, %s, %s)"
#     # cur.execute(sql, data['positionName'], data['companyShortName'], data['city'])
#     #
#     # cur.close() #关闭游标
#     # conn.commit()
#     # conn.close()

