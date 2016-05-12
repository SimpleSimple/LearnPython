#! usr/bin/env python
# coding:utf-8


#import urllib.request
#from urllib import request
import requests
import mysql.connector

keywordindex='python'
city=''

r = requests.get('http://www.lagou.com/jobs/positionAjax.json?px=default&first=true&city='+city+'&kd='+keywordindex+'&pn=1')
# print(type(r.json()))
# count = int(r.json()['content']['result'])
pagecount = int(r.json()['content']['totalPageCount'])  #总页数

f = open('companName.txt', 'w')
for i in list(range(0, pagecount)):
    if i == 1:
        type='true'
    else :
        type='false'
    r = requests.get('http://www.lagou.com/jobs/positionAjax.json?px=default&first='+type+'&city='+city+'&kd='+keywordindex+'&pn='+str(i+1)+'')
    jsondata = r.json()['content']['result']
    # print(jsondata)
    for t in list(range(len(jsondata))):
        # print(jsondata[t]['companyShortName'])
        f.write(jsondata[t]['companyShortName']+'  '+jsondata[t]['positionName']+'  '+jsondata[t]['createTime']+'\n')
    print('正在抓取搜索页面第%d页,还剩下%d页'%(i+1, pagecount-i-1))

f.close()
print('Program over!')




