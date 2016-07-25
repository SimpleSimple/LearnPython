# -*- coding: utf-8 -*-
# title: 图片抓取

import urllib.request
import re, os

url="http://www.zhihu.com"

req = urllib.request.Request(url)
page = urllib.request.urlopen(req)
html = page.read().decode('gbk', 'ignore')

# 匹配图片正则
reg = r'src="(.+?\.jpg)"'
imgre = re.compile(reg)
imglist = re.findall(imgre, html)

targetDir = r'F:\pic'

for imgurl in imglist:
    print(imgurl)
    pos = imgurl.rindex('/')
    t = os.path.join(targetDir, imgurl[pos+1:])

    try:
        urllib.request.urlretrieve(imgurl, t)
    except:
        print("IOError")










