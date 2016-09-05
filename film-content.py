import requests
from bs4 import BeautifulSoup
import re
import time

def film_douban(page):
    num = 0
    file = open('H:\豆瓣编号/1.txt')
    line = file.readlines(100000)
    while num <= page:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
            url = 'http://movie.douban.com/subject/'+ str(line[num])
            response = requests.get(url, headers=headers, timeout=60)
            content = response.text
            rank = re.findall('<span property="v:summary" class="">.*?\u3000\u3000(.*?)\n                        </span>|<span class="all hidden">\n                                \u3000\u3000(.*?)\n                        </span>', content, re.S)
            num += 1
            for ranks in rank:
                str_ranks = str(ranks)
                contents = str_ranks.replace('(\'\', \'','').replace('(\'','').replace('\\n                                    <br />\\n                                \\u3000\\u3000','').replace('\')','').replace('\', \'','')
                f = open('g://douban1.txt','a',encoding='utf-8')
                f.write(contents)
                f.write('\n')
                f.close()

            time.sleep(1)
        except:
            print(str(line[num]) + '出错了')


film_douban(100000)