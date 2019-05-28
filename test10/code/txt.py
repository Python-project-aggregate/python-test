import requests
import lxml
import random
import time
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}  # 可以通过抓包工具获取,模拟浏览器
proxy = {'112.95.25.61:8088'}  # 代理的IP,也可以自己在网上找
while True:
    # 要刷的文章
    url1 = 'https://blog.csdn.net/admin243950/article/details/90575757'
    url2 = 'https://blog.csdn.net/admin243950/article/details/90576074'
    url3 = 'https://blog.csdn.net/admin243950/article/details/90576077'
    url4 = 'https://blog.csdn.net/admin243950/article/details/90576072'
    url5 = 'https://blog.csdn.net/admin243950/article/details/90576072'
    url6 = 'https://blog.csdn.net/admin243950/article/details/90576072'
    url7 = 'https://blog.csdn.net/admin243950/article/details/90576072'

    Url = [url1, url2, url3, url4, url5, url6, url7]
    url = random.choice(Url)  # 随机随机访问上面的文章
    print(url, "*" * 30)
    time.sleep(0.6)  # 设置访问的时间
    response = requests.get(url, headers=headers, proxies=proxy).content.decode('utf-8')
    mytree = lxml.etree.HTML(response)
    csdnlist = mytree.xpath('//div[@class="article-list"]/div')
    for i in csdnlist:
        try:
            iUrl = i.xpath('./h4/a/@href')[0]

        except:
            response = requests.get(url= iUrl, headers=headers, proxies=proxy).content.decode('utf-8')
            time.sleep(0.8)
            # 和上面一样的随机访问其他的文章
            urla = 'https://blog.csdn.net/admin243950/article/details/90575757'
            urlb = 'https://blog.csdn.net/admin243950/article/details/90575752'
            urlc = 'https://blog.csdn.net/admin243950/article/details/90575747'
            urld = 'https://blog.csdn.net/admin243950/article/details/90575744'
            URL = [urla, urlb, urlc, urld]
            urll = random.choice(URL)
            response1 = requests.get(url=urll, headers=headers, proxies=proxy).content.decode('utf-8')
            # print(response1)
            # print(response)
            print(urll, "$" * 30)
            print(iUrl, "@" * 30)