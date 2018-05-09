from bs4 import BeautifulSoup

from urllib.request import urlopen

html = urlopen("http://www.hneeb.cn/2018/website/newsDoc/zlzx/2012223111521.html"
               ).read().decode('GBK')

soup = BeautifulSoup(html,features='lxml')

##print (soup)

all_herf= soup.find_all('a')
t_html=[]

for i in all_herf:
    print(i['href'])
