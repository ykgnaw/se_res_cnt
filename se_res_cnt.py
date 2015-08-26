# -*- coding: gbk -*-
import urllib2
import re


def search(keyword):
    url = 'http://www.baidu.com/s?wd=' + keyword
    html = urllib2.urlopen(url).read()
    f = open('nihao.html','wb')
    f.write(html)
    f.close()

if __name__ == '__main__':
    keyword = raw_input('enter key word:')
    search(keyword)