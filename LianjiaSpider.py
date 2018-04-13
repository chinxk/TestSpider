from bs4 import BeautifulSoup
import requests
import time
import json
import csv

global url, headers
# url = 'https://cd.lianjia.com'
url = 'https://bj.lianjia.com'
headers = {'Host': "bj.lianjia.com",
           'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           'Accept-Encoding': "gzip, deflate, br",
           'Cookie': "lianjia_uuid=75556348-6be5-462b-849e-5177294f737d; _jzqa=1.179377831565160860.1504152836.1522994803.1523507175.20; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1522994802; _smt_uid=59a78d08.4689c276; _qzja=1.407199939.1504152845121.1522994802874.1523507175314.1523507385720.1523507400166.0.0.0.102.20; CNZZDATA1253492306=1668246086-1504149006-https%253A%252F%252Fbj.lianjia.com%252F%7C1523502400; CNZZDATA1254525948=1485164074-1504150132-https%253A%252F%252Fbj.lianjia.com%252F%7C1523502829; CNZZDATA1255633284=414942645-1504148916-https%253A%252F%252Fbj.lianjia.com%252F%7C1523505250; CNZZDATA1255604082=1443022272-1504151495-https%253A%252F%252Fbj.lianjia.com%252F%7C1523504546; gr_user_id=fe8f1b74-9877-4b61-b758-d37821dad1e3; _ga=GA1.2.148941542.1504153266; all-lj=6341ae6e32895385b04aae0cf3d794b0; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1523507398; UM_distinctid=16299906f64c5-0bc01269ccddf88-49536a-13c680-16299906f6669c; _jzqc=1; _jzqy=1.1522994803.1522994803.1.jzqsr=baidu.-; _qzjc=1; select_city=510100; lianjia_ssid=2f5ce8a7-0c6c-461a-8995-4d97dcb30b30; gr_session_id_a1a50f141657a94e=f8c8f1c1-1820-4bb6-8c07-6fa5fad32cb3; _jzqb=1.11.10.1523507175.1; _jzqckmp=1; _qzjb=1.1523507175314.11.0.0.0; _qzjto=11.1.0; _gid=GA1.2.819461535.1523507178",
           'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}


def get_info(href):
    r = requests.get(url + href, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    time.sleep(0.5)
    ul = soup.find('ul', attrs={'class': 'listContent'})
    time.sleep(0.5)
    lis = ul.find_all('li', limit=30)
    info_list = []

    for li in lis:
        try:
            info = li.find('div', attrs={'class': 'info'})
            title = info.find('div', attrs={'class': 'title'}).text
            deal_date = info.find('div', attrs={'class': 'dealDate'}).text
            total_price = info.find('div', attrs={'class': 'totalPrice'}).text.replace('万', '')
            unit_price = info.find('div', attrs={'class': 'unitPrice'}).span.text
            if isnum2(total_price):
                # info = {'title': title, 'd_date': deal_date, 't_price': total_price, 'u_price': unit_price}
                deal_ym = deal_date[0:len(deal_date) - 3].replace('.', '/')
                info = [title, deal_ym, total_price, unit_price]
                info_list.append(info)
            else:
                print(total_price)
        except AttributeError:
            print('can\'t get Attribute')
    print(info_list)
    return info_list


def get_page_num(href):
    r = requests.get(url + href, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    page_json = soup.find('div', attrs={'comp-module': 'page'}).get('page-data')
    t_page_num = json.loads(page_json)['totalPage']
    # result_num = len(page_group_a.find_all('a'))
    print(t_page_num)
    return t_page_num


def isnum2(s):
    try:
        float(s)
        return True
    except:
        return False

if __name__ == '__main__':

    # file_names = ['成都.csv', '城南.csv']
    file_names = ['北京.csv', '海淀.csv']
    tgt_h_lst = []
    # tgt_h_lst.append(['jiuyanqiao', 'dongdalu', 'shuinianhe', 'babaojie', 'taishenglu', 'jianshelu', 'lijiatuo'])
    # tgt_h_lst.append(['jinrongcheng','dayuan', 'xinhuizhan', 'huayang', 'sihe'])
    tgt_h_lst.append(['jinrongjie','dongsi1'])
    tgt_h_lst.append(['xierqi1', 'xibeiwang'])

    for i in range(2):
        out = open('.\data\\' + file_names[i], 'w', newline='')
        csv_writer = csv.writer(out)
        for tgt_h in tgt_h_lst[i]:
            href_start = "/chengjiao/%s/ng1" % (tgt_h)
            page_num = get_page_num(href_start)
            result_list = []
            for c_page in range(1, page_num + 1):
                c_href = "/chengjiao/%s/pg%sng1/" % (tgt_h, str(c_page))
                print(c_href)
                result_list += get_info(c_href)
            print(len(result_list))
            csv_writer.writerows(result_list)
