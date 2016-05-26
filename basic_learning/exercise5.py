# -*- coding: utf-8 -*-

import urllib.request
import re

page = urllib.request.urlopen('https://www.zhihu.com/question/30116337')
html = page.read().decode('gbk', 'ignore')
print(html)

reg = r'src="(.+?\.jpg)"'
imgre = re.compile(reg)
imglist = re.findall(imgre, html)

for imgurl in imglist:
    print(imgurl)