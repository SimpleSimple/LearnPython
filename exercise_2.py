# coding:utf-8

# # import urllib.request   # python 3.x 引入要用urllib.request
# f= urllib.request.get('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000')
# cnt = f.read()
# f.close()

# 使用requests库
import requests

# 获取HTML网页内容
f= requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
cnt = f.content

print(type(cnt))



# 列表生成器
L = []
for x in range(1,11):
    L.append(x * x)

print(L)

