# -*- coding: utf-8 -*-

import urllib.request
import re, os

# rindex
# str.rindex(str, beg=0 end=len(string))

# url = "http://www.meizitu.com/a/4674.html"
# url = "http://tu.duowan.com/m/meinv/"
url = "http://www.zhihu.com/explore#monthly-hot"
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Connection": "keep-alive",
#     "Cookie":'d_c0="ACDAScIH5QmPTntBfBt098GJ-C71qBJYbY0=|1462768786"; _za=63ab5974-7be8-4e55-ad97-87836d5464bb; _zap=0bbc7c6e-e05b-499b-91db-215cf16da404; q_c1=90881a3d0cc248c8a5cb4fee8f6a0844|1463489437000|1463489437000; __utmt=1; __utma=51854390.669040370.1462768788.1464255402.1464674773.8; __utmb=51854390.2.10.1464674773; __utmc=51854390; __utmz=51854390.1463651956.5.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.000--|3=entry_date=20160517=1; l_n_c=1; l_cap_id="ZTRmMzk0YTE1ODRhNDYyYTg2N2VhNGI3Nzk1ZmE1NjI=|1464674777|60dd407321671f3c1e0a9daf5d2d328a396f13de"; cap_id="NmI3Mjg1MzE4MzMwNDg1ZWFiOTkzYmJlNWNmNDhjZGM=|1464674777|59735bbd39875cc52f2656e8107564923ca0e679"; n_c=1',
#     "Host": "www.zhihu.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
# }
# req = urllib.request.Request(url, headers = headers)  #带headers模拟浏览器发送请求信息
req = urllib.request.Request(url)
page = urllib.request.urlopen(req)
html = page.read().decode('gbk', 'ignore')

link_reg = r'<a.*?href="(.+)".*?>(.*?)</a>'
linkre = re.compile(link_reg)
linklist = re.findall(linkre, html)
print(linklist)


# 图片爬取
# reg = r'src="(.+?\.jpg)"'
# imgre = re.compile(reg)
# imglist = re.findall(imgre, html)
#
# targetDir = r'F:\pic'
#
# for imgurl in imglist:
#     pos = imgurl.rindex('/')
#     t = os.path.join(targetDir, imgurl[pos+1:])
#     print("fileurl:" + imgurl + " filename:"+t)
#     # with open(t, 'wb') as file:
#     #     file.write(imgurl.encode('utf-8'))
#     try:
#         urllib.request.urlretrieve(imgurl, t)
#     except:
#         print("IOError")




