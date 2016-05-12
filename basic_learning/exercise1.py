# coding:utf-8
__author__ = 'Administrator'

import requests
import json


# http://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E

keywordindex='Android'
post_data={'first':'true','pn':1,'kd':keywordindex}

r=requests.post('http://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E', data=post_data)
data=r.content
# print(str(data,encoding='utf-8'))
# print(json.loads(str(data,encoding='utf-8'))['content'])
urlcount=int(json.loads(str(data,encoding='utf-8',errors='ignore'))['content']['totalPageCount'])
print('本次搜索页面共计%d'%urlcount)

for i in list(range(0,urlcount)):
    post_data={'pn':i,'kd':keywordindex}
    r=requests.post('http://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E',data=post_data)
    data=r.content
    array=json.loads(str(data,encoding='utf-8',errors='ignore'))['content']['result']
    for j in list(array):
        # print(type(list[j]['companyShorName']))
        print(list[j])
    # print(json.loads(str(data,encoding='utf-8',errors='ignore'))['content']['result'])