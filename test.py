#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup


########################################################################
def usage():
    print("\nUsage: test.py <URL>\n")
    return

def main():
    if len(sys.argv) < 2:
        #usage()
        #return
        url = "http://www.hneeb.cn/2018/website/newsDoc/zlzx/2012223111521.html"
    else:
        url = sys.argv[1]

    res = requests.get(url)

    #print("Get web page from: " + res.url)

    print("Web page text: " + res.text)

    soup = BeautifulSoup(res.text, "lxml")

    print soup.a.attrs

    print soup.find_all('a')

    return

########################################################################
if __name__ == "__main__":
    # execute only if call as a script
    main()

