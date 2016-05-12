__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import requests,re,json
from urllib import request

def lagou_spider(keyword):
    #将搜索字符串转换为utf-8编码，之后进行lagou.com搜索url构造
    keywordbyte=keyword.encode('utf-8')
    keywordindex=str(keywordbyte).replace(r'\x','%').replace(r"'","")
    keywordindex=re.sub('^b','',keywordindex)

    type='true'
    url='http://www.lagou.com/jobs/positionAjax.json?px=default&first='+type+'&kd='+keywordindex+'&pn=1'
    with request.urlopen(url) as f:
        data=f.read()
        print(data)
        count = int(json.loads(str(data,encoding='utf-8',errors='ignore'))['content']['totalCount'])
        print(count)

    for i in list(range(0, count)):
        if i==0:
            type = 'true'
        else:
            type= 'false'
        url='http://www.lagou.com/jobs/positionAjax.json?px=default&first='+type+'&kd='+keywordindex+'&pn='+str(i+1)
        print(url)
        with request.urlopen(url) as f:
            data =f.read()
            print(data)

if __name__=='__main__':
    keyword = input("请输入搜索词(回车进入下一步): ")
    #keyword='数据挖掘' #可以随意定义搜索词
    lagou_spider(keyword)