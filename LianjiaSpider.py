from bs4 import BeautifulSoup
from bs4 import re
import requests


def get_info(href):
    url = 'https://cd.lianjia.com' + href
    headers = {'Host': "cd.lianjia.com",
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               'Accept-Encoding': "gzip, deflate, br",
               'Cookie': "lianjia_uuid=75556348-6be5-462b-849e-5177294f737d; _jzqa=1.179377831565160860.1504152836.1522994803.1523507175.20; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1522994802; _smt_uid=59a78d08.4689c276; _qzja=1.407199939.1504152845121.1522994802874.1523507175314.1523507385720.1523507400166.0.0.0.102.20; CNZZDATA1253492306=1668246086-1504149006-https%253A%252F%252Fbj.lianjia.com%252F%7C1523502400; CNZZDATA1254525948=1485164074-1504150132-https%253A%252F%252Fbj.lianjia.com%252F%7C1523502829; CNZZDATA1255633284=414942645-1504148916-https%253A%252F%252Fbj.lianjia.com%252F%7C1523505250; CNZZDATA1255604082=1443022272-1504151495-https%253A%252F%252Fbj.lianjia.com%252F%7C1523504546; gr_user_id=fe8f1b74-9877-4b61-b758-d37821dad1e3; _ga=GA1.2.148941542.1504153266; all-lj=6341ae6e32895385b04aae0cf3d794b0; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1523507398; UM_distinctid=16299906f64c5-0bc01269ccddf88-49536a-13c680-16299906f6669c; _jzqc=1; _jzqy=1.1522994803.1522994803.1.jzqsr=baidu.-; _qzjc=1; select_city=510100; lianjia_ssid=2f5ce8a7-0c6c-461a-8995-4d97dcb30b30; gr_session_id_a1a50f141657a94e=f8c8f1c1-1820-4bb6-8c07-6fa5fad32cb3; _jzqb=1.11.10.1523507175.1; _jzqckmp=1; _qzjb=1.1523507175314.11.0.0.0; _qzjto=11.1.0; _gid=GA1.2.819461535.1523507178",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    ul = soup.find('ul', attrs={'class': 'listContent'})
    lis = ul.find_all('li')
    info_list = []

    for li in lis:
        info = li.div
        title = info.find('div', attrs={'class': 'title'}).text
        deal_date = info.find('div', attrs={'class': 'dealDate'}).text
        total_price = info.find('div', attrs={'class': 'totalPrice'}).text
        unit_price = info.find('div', attrs={'class': 'unitPrice'}).span.text
        info = {'title': title, 'd_date': deal_date, 't_price': total_price, 'u_price': unit_price}
        info_list.append(info)

    # print(info_list)


if __name__ == '__main__':
    url = 'https://cd.lianjia.com/chengjiao/c3011053889173/'
    headers = {'Host': "cd.lianjia.com",
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               'Accept-Encoding': "gzip, deflate, br",
               'Cookie': "lianjia_uuid=75556348-6be5-462b-849e-5177294f737d; _jzqa=1.179377831565160860.1504152836.1522994803.1523507175.20; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1522994802; _smt_uid=59a78d08.4689c276; _qzja=1.407199939.1504152845121.1522994802874.1523507175314.1523507385720.1523507400166.0.0.0.102.20; CNZZDATA1253492306=1668246086-1504149006-https%253A%252F%252Fbj.lianjia.com%252F%7C1523502400; CNZZDATA1254525948=1485164074-1504150132-https%253A%252F%252Fbj.lianjia.com%252F%7C1523502829; CNZZDATA1255633284=414942645-1504148916-https%253A%252F%252Fbj.lianjia.com%252F%7C1523505250; CNZZDATA1255604082=1443022272-1504151495-https%253A%252F%252Fbj.lianjia.com%252F%7C1523504546; gr_user_id=fe8f1b74-9877-4b61-b758-d37821dad1e3; _ga=GA1.2.148941542.1504153266; all-lj=6341ae6e32895385b04aae0cf3d794b0; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1523507398; UM_distinctid=16299906f64c5-0bc01269ccddf88-49536a-13c680-16299906f6669c; _jzqc=1; _jzqy=1.1522994803.1522994803.1.jzqsr=baidu.-; _qzjc=1; select_city=510100; lianjia_ssid=2f5ce8a7-0c6c-461a-8995-4d97dcb30b30; gr_session_id_a1a50f141657a94e=f8c8f1c1-1820-4bb6-8c07-6fa5fad32cb3; _jzqb=1.11.10.1523507175.1; _jzqckmp=1; _qzjb=1.1523507175314.11.0.0.0; _qzjto=11.1.0; _gid=GA1.2.819461535.1523507178",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    href_list = []
    page_group_a = soup.find('div', attrs={'class': 'pagination_group_a'})
    page_num = 0
    for a in page_group_a.find_all('a'):
        page_num += 1
    print(page_num)
