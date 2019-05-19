import time
import re
# <img src="(.*?)" alt=".*?" /><br/>
import requests
import multiprocessing
from multiprocessing import Pool
MAX = multiprocessing.cpu_count()
t1 = time.time()
patten = re.compile('<img src="(.*?)" alt=".*?" /><br/>', re.S)
urls = ['http://5468.xyz/clhr_{}.html'.format(
    i) for i in range(780000, 790000)]
def job(url):
    n = 0
    r = requests.get(url)
    html = r.text
    if r.status_code == 200:
        img =re.findall(patten, html)
        for i in img:
            n += 1
            print(n)
            img_ = requests.get(i)
            with open('E:/img/' + str(n) + '.jpg', 'wb') as f:
                f.write(img_.content)


if __name__ == '__main__':

    p = Pool(MAX)
    for url in urls:
        p.apply_async(job, args = (url,))
    p.close()
    p.join()
    print(time.time()-t1)
