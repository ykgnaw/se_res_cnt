# -*- coding: utf-8 -*-
import urllib2
import re
import sys
reload(sys)

sys.setdefaultencoding('utf8')

def baidu_search(keyword):
    url = "http://www.baidu.com/s?wd=%s"%(keyword)
    html = urllib2.urlopen(url).read()

    #html = '<div class="result c-container aaa背负,才能最好地放下</div></div>'
    #content = unicode(html, 'gbk', 'ignore')
    #content = unicode(html, 'utf8', 'ignore')

    pattern = re.compile(r'<div class="result c-container[\s\S]*?><em>%s</em>[\s\S]*?</div></div>'%keyword)
    resList = pattern.findall(html)
    i = 0
    for res in resList:
        i += 1
        print '%d'%i + res

  #  f = open('nihao.html','wb')
   # f.write(html)
    #f.close()

if __name__ == '__main__':
    inputword = raw_input('enter key word:')
    baidu_search(inputword)
