import re

import requests
from bs4 import BeautifulSoup


def get_page(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


def parse_page(html, return_list):
    soup = BeautifulSoup(html, 'html.parser')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()
        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = ''
        lowtem = day.find('p', 'tem').find('i').get_text()
        win = re.findall('(?<= title=").*?(?=")', str(day.find('p', 'win').find('em')))
        wind = '-'.join(win)
        level = day.find('p', 'win').find('i').get_text()
        return_list.append([date, wea, lowtem, hightem, wind, level])


def main():
    # 101210101Hangzhou
    url = 'http://www.weather.com.cn/weather/101210101.shtml'
    html = get_page(url)
    wea_list = []
    parse_page(html, wea_list)
    return wea_list[0][1]


if __name__ == "__main__":
    main()
