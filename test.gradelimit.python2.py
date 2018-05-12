#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re   # for detecting charset in html
import requests
from bs4 import BeautifulSoup
#from urllib.request import urlopen


def getCharset(html):
    pat = re.compile(r'charset\s*=([a-zA-Z0-9-_]*)[ \t\n\r\f\v">]', re.M | re.I)

    m = pat.search( html, re.M | re.I )

    if m == None :
        return ""
    else:
        return m.group(1)


reload(sys)
sys.setdefaultencoding('utf8')

urls=[
'http://www.hneeb.cn/website/newsDoc/zkdt/2016717134751.htm',
'http://www.hneeb.cn/website/newsDoc/zkdt/2015714225749.htm',
'http://www.hneeb.cn/website/newsDoc/jyrd/2014714234713.htm',
'http://www.hneeb.cn/website/newsDoc/jyrd/201371605325.htm',
'http://www.hneeb.cn/website/newsDoc/jyrd/201271612343.htm',
'http://www.hneeb.cn/website/newsDoc/jyrd/201171304727.htm',
'http://www.hneeb.cn/website/newsDoc/zkdt/201071315633.html',
'http://www.hneeb.cn/website/newsDoc/zkdt/20097131541.html',
'http://www.hneeb.cn/website/newsDoc/zkdt/200871311951.html',
'http://www.hneeb.cn/website/newsDoc/zkdt/200771332431.html',
'http://www.hneeb.cn/website/newsDoc/zkdt/200671355723.html']

filenames=['2016.txt','2015.txt','2014.txt','2013.txt','2012.txt',
          '2011.txt','2010.txt','2009.txt','2008.txt','2007.txt','2006.txt']


for i,j in zip(urls, filenames):
    f=open(j,'w+')
    try:
        print("\nFetching web page at: " + i + "\n")
        #html=urlopen(i)
        r = requests.get(i)
        charset = getCharset(r.content)
        print( "\nWeb page encoding is: " + charset + "\n" )
        r.encoding = charset
        soup=BeautifulSoup(r.content, features = 'lxml') # after using r.content instead of r.text, encoding of txt file is correct
                                                        # however, I don't know why
        if soup.find('tr'):
            table = soup.find_all('tr')
            print("\nWriting to file: " + j + "\n")
            for k in table:
                f.write(k.get_text())
    except Exception as e:
        print("error!"+j)
        print(e)
        f.close()
        continue
    f.close()
