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




#  拿到链接，用的urllib2打开后获取到整个页面，用lmxl解析获取到的整个页面。
#  遍历在这个页面想要拿到的数据的标签
#  urllib2.urlopen（urllib2.Request（链接））
#  BeautifulSoup（整个页面， 'LXML'）
#  find_all全部（'标签'，'标识'）标识例如class
