import re
import requests
url = 'https://www.lanse9.com/'
urls = requests.get(url)
print(urls.text)