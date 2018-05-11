from bs4 import BeautifulSoup
from urllib.request import urlopen




https=[
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

name_txts=['2016.txt','2015.txt','2014.txt','2013.txt','2012.txt',
          '2011.txt','2010.txt','2009.txt','2008.txt','2007.txt','2006.txt']


http2017='http://www.hneeb.cn/website/newsDoc/jyrd/2017718165024.htm'
name_txt2017='2017.txt'
f=open(name_txt2017,'w+')
try:
    html=urlopen(http2017)
    soup=BeautifulSoup(html,features='lxml')
    if soup.find('tr'):
        table = soup.find_all('tr')
        for k in table:
            f.write(k.get_text())
except Exception as e:
    print("error!"+j)
    print(e)
finally:
    f.close()
    

for i,j in zip(https,name_txts):
    f=open(j,'w+')
    try:
        html=urlopen(i)
        soup=BeautifulSoup(html,features='xml')
        if soup.find('tr'):
            table = soup.find_all('tr')
            for k in table:
                f.write(k.get_text())
    except Exception as e:
        print("error!"+j)
        print(e)
        f.close()
        continue
    f.close()
