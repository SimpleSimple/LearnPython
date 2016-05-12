# coding:utf-8

__author__ = 'Administrator'

import requests
import re
import json

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
r=requests.get('https://www.github.com/timeline.json', timeout=6)
print(r.json())
print('Print Json Message:')
print(r.json()['documentation_url'])



r=requests.get('https://www.zhihu.com/question/30116337')
print(r.content)


# print(re.match('zh-question-title.+?<h2.+?>(.+?)</h2>', r.text))

m=re.search(r'zh-question-title.+?<h2.+?>(.+?)</h2>',r.text)

print(m)

m1=re.search(r'zh-question-title.+?<h2.+?>(.+?)</h2>','<div id="zh-question-title" data-editable="true">\n\n<h2 class="zm-item-title zm-editable-content">\n\n\xe5\xa4\xa7\xe8\x83\xb8\xe5\xa5\xb3\xe7\x94\x9f\xe6\x80\x8e\xe4\xb9\x88\xe6\x8b\x8d\xe5\xb0\x8f\xe6\xb8\x85\xe6\x96\xb0\xe7\x85\xa7\xe5\xa5\xbd\xe7\x9c\x8b\xef\xbc\x9f\n\n</h2>')
print(m1)

pattern=re.compile('zh-question-title.+?<h2.+?>(.+?)</h2>')
m2=re.search(pattern, 'id="zh-question-title" <h2>sssss</h2>')
print(m2)


# 检查类型
list = json.loads(str('[{"createTime":"2016-05-05 16:34:53","companyId":122145,"adjustScore":0,"positionName":"网络推广","companyName":"高浪灯光","education":"大专","city":"广州","positionType":"运营","positionId":1650973,"financeStage":"成熟型(D轮及以上)","companyShortName":"广州高浪电子科技有限公司","companyLogo":"i/image/M00/1A/86/Cgp3O1b6RNOAAdIyAAC6NKvPmTQ858.jpg","salary":"6k-8k","industryField":"电子商务","deliverCount":0,"positionAdvantage":"7小时工作时，不用外出，包吃住","companyLabelList":[],"jobNature":"全职","workYear":"1-3年","positionFirstType":"运营","score":0,"leaderName":"暂没有填写","companySize":"50-150人","formatCreateTime":"16:34发布","calcScore":false,"orderBy":66,"showOrder":0,"haveDeliver":false,"adWord":0,"randomScore":0,"countAdjusted":false,"relScore":0,"imstate":"disabled","createTimeSort":1462437293000,"positonTypesMap":null,"hrScore":17,"flowScore":0,"showCount":31,"pvScore":7.536407063294263,"plus":"否","totalCount":0,"searchScore":0.0},{"createTime":"2016-05-05 16:34:51","companyId":122145,"adjustScore":0,"positionName":"外贸业务员（舞台灯光）","companyName":"高浪灯光","education":"学历不限","city":"广州","positionType":"销售","positionId":1700305,"financeStage":"成熟型(D轮及以上)","companyShortName":"广州高浪电子科技有限公司","companyLogo":"i/image/M00/1A/86/Cgp3O1b6RNOAAdIyAAC6NKvPmTQ858.jpg","salary":"3k-6k","industryField":"电子商务","deliverCount":0,"positionAdvantage":"朝九晚五，包食宿，购买社保，出国机会","companyLabelList":[],"jobNature":"全职","workYear":"1-3年","positionFirstType":"市场与销售","score":0,"leaderName":"暂没有填写","companySize":"50-150人","formatCreateTime":"16:34发布","calcScore":false,"orderBy":66,"showOrder":0,"haveDeliver":false,"adWord":0,"randomScore":0,"countAdjusted":false,"relScore":0,"imstate":"disabled","createTimeSort":1462437291000,"positonTypesMap":null,"hrScore":17,"flowScore":0,"showCount":70,"pvScore":15.04733474733546,"plus":"否","totalCount":0,"searchScore":0.0}]'))
print(list)
print(len(list))
for i in range(0, len(list)):
    print(list[i]['companyShortName'])
    print(list[i]['industryField'])
    print(list[i]['city'])
    print(list[i]['salary'])
    print(list[i]['positionName'])
    print('-------------------------------')



