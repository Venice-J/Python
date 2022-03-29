import requests as rq
from bs4 import BeautifulSoup 

# 要爬取的網址
url ='https://www.vscinemas.com.tw/vsweb/film/coming.aspx'

# 增加 http header user-agent 讓網站以為是正常的瀏覽使用者
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

# 發出 HTTP GET request
resp = rq.get(url, headers=headers)
# 網頁編碼方式
resp.encoding = 'UTF-8'
soup = BeautifulSoup(resp.text, "html.parser")
# 印出

section_times = soup.find_all('section','infoArea')

for item in section_times:
    name = item.find('h2').a.text
    date = item.find('time').text
    print(f'電影名稱：{name}\n上映日期：{date}\n===================================')