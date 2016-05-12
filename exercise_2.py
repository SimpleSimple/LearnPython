# coding:utf-8

import urllib


# 获取HTML网页内容
f= urllib.urlopen("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
cnt = f.read()
f.close()

print(cnt)