import re
import requests
from multiprocessing import Pool
url = requests.get('https://www.lansedaohang.club/')
url.encoding = 'UTF-8'
html = url.text
pattern = re.compile('''<li><a href="(http.*?)"   rel="external nofollow" target="_blank">.*?</a></li>''',re.M)
page = re.findall(pattern, html)
# print(page)
lst = []
def get_page(url):
    r = requests.get(url)
        # r.encoding = 'UTF-8'
    if r.status_code == 200:
        print(url, r.elapsed.total_seconds())
        # lst.append(url)
    # print(lst)

if __name__ == '__main__':
    p = Pool(8)
    for url in page:
        p.apply_async(get_page, args = (url,))
    p.close()
    p.join()
    # print(*lst, sep='\n')
