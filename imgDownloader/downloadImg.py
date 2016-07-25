#author:lenglingx@gmail.com
#date:2014-12-08

# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        pass
    def handle_starttag(self,tag,attrs):
        #print("Encountered a start tag:",tag)
        if tag == "img":
            s = []
            for (variable, value) in attrs:
                s.append(value)
            #print("ss:",s)
            self.links.append(s)
            s = []
        pass

    def handle_endtag(self,tag):
        #print("Encountered a end tag:",tag)
        pass
    def handle_data(self,data):
        #print("Encountered some data:",data)
        pass



def geturl(url):
    req = urllib.request.urlopen(url)
    req = req.read()
    return req.decode("gbk")


def continsrc(src):
    inta = src.find("<div id=\"picture\">")
    #print(inta) 所找的第一个位置点
    intb = src.find("<div class=\"boxinfo\">")
    #print(intb) 所找的第二个位置点
    content = src[inta:intb]
    return content


def pageinurl(url):
    src = geturl(url)
    content = continsrc(src)
    parser = MyHTMLParser()
    parser.feed(content)
    parser.close()
    alinks = parser.links
    for i in range(len(alinks)):
        print("filename:",alinks[i][0],"fileurl:",alinks[i][1])
        urllib.request.urlretrieve(alinks[i][1],alinks[i][0]+".jpg")
    print("ok!!")


if __name__ == "__main__":
    print("------------------------")
    #url = "http://www.meizitu.com/a/4647.html"
    url = "http://www.meizitu.com/a/4674.html"
    src = geturl(url)

    content = continsrc(src)
    print(content)

    parser = MyHTMLParser()
    parser.feed(content)
    parser.close()

    print("------------------------------------------")
    print(parser.links)

    a = parser.links
    b = len(a)
    print(len(a))

    for i in range(b):
        print("filename:",a[i][0],"fileurl:",a[i][1])
        urllib.request.urlretrieve(a[i][1],a[i][0]+".jpg")


    print("==================================")
    pageinurl("http://www.meizitu.com/a/4647.html")