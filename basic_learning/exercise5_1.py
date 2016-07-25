# coding:utf-8

import urllib.request
import os
import queue

myQueue = queue.Queue(10)

# s = '我是愤怒'
# print(type(s))
# s2 = u'我是愤怒'
# print(type(s2))
# print(type(s.encode('utf-8')))

def geturl():
    if os.path.exists('url.txt'):
        f = open('url.txt', 'r+')
        while 1:
            link = f.readline()
            if not link:
                break
            # print('----------------------')
            print(link)
            myQueue.put(link)
    else:
        print('File not exists!')

def worker():
    while 1:
        item = myQueue.get()
        do_work(item)
    return

def do_work(url):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    # gbk编码中文乱码
    # html = page.read().decode('gbk', 'ignore')
    html = page.read().decode('utf-8','ignore')
    # print(html.encode)
    # html = html.encode('utf-8')
    f = open('1.html', 'r+')
    f.write(html)
    print(html)

if __name__=="__main__":
    geturl()
    worker()