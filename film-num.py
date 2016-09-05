import requests
from bs4 import BeautifulSoup
import re
import time
def douban_spider(ten):
    toplimit = 100
    downlimit = 90
    while toplimit >= ten:
        try:
            url = 'http://movie.douban.com/j/chart/top_list?type=32&interval_id=' + str(toplimit) + '%3A' + str(downlimit) + '&action=&start=0&limit=1000'
            response = requests.get(url, timeout=60)
            content = response.text
            contents = re.findall('subject\\\\/(.*?)\\\\/"',content,re.S)
            toplimit -= 5
            downlimit -= 5
            for num in contents:
                print(num)
            time.sleep(3)
        except:
            print('出错了' + str(toplimit) + ' ' + str(downlimit))


douban_spider(10)