import re
import requests
url = requests.get('https://www.lansedaohang.club/')
url.encoding = 'UTF-8'
html = url.text
pattern = re.compile('''<li><a href="(http.*?)"   rel="external nofollow" target="_blank">(.*?)</a></li>''',re.M)
page = re.findall(pattern, html)
for i in page:
    r = requests.get(i[0])
    if r.status_code==200:
        print(i[0],i[1])