import urllib2
from bs4 import BeautifulSoup
def aaa():
    url = "https://www.v2ex.com"
    res = urllib2.urlopen(urllib2.Request(url))
    print res.code
    data = res.read()
    soup = BeautifulSoup(data,"lxml")
    data = soup.find_all('span',"item_title")
    with open('D:1.txt','w') as f:
        for list in data:
            name = list.find("a").string.encode('utf-8')
            href = url + list.find("a").get("href").encode('utf-8')
            f.write(name+"       "+href+'\n')
    f.close()
    return "1"
print aaa()