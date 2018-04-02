import requests
import json


def get_json():
    # url = 'https://sijipiao.fliggy.com/ie/flight_search_result_poller.do?supportMultiTrip=true&searchBy=1281&searchJourney=[{"depCityCode":"CTU","arrCityCode":"MAD","depCityName":"%E6%88%90%E9%83%BD","arrCityName":"%E9%A9%AC%E5%BE%B7%E9%87%8C","depDate":"2018-03-31","selectedFlights":[]},{"depCityCode":"MAD","arrCityCode":"CTU","arrCityName":"%E6%88%90%E9%83%BD","depCityName":"%E9%A9%AC%E5%BE%B7%E9%87%8C","depDate":"2018-04-07","selectedFlights":[]}]&tripType=1&searchCabinType=0&agentId=-1&searchMode=0&b2g=0&formNo=-1&cardId=&needMemberPrice=&callback=miniLoadPreload'
    url = 'https://sijipiao.fliggy.com/ie/flight_search_result_poller.do'
    params = {'supportMultiTrip': 'true',
              'searchBy': '1281',
              'searchJourney': '[{"depCityCode":"CTU","arrCityCode":"MAD","depCityName":"","arrCityName":"","depDate":"2018-03-31","selectedFlights":[]},{"depCityCode":"MAD","arrCityCode":"CTU","arrCityName":"","depCityName":"","depDate":"2018-04-07","selectedFlights":[]}]',
              'tripType': '1',
              'searchCabinType': '0',
              'agentId': '-1',
              'searchMode': '0',
              'b2g': '0',
              'formNo': '-1',
              'cardId': '',
              'callback': "miniLoadPreload",
              'needMemberPrice': 'true'}
    headers = {'Host': "sijipiao.fliggy.com",
               # 'Referer': "https://sijipiao.fliggy.com/ie/flight_search_result.htm?spm=181.7310117.a321p.4.696e2e12ZL6W9W&depCityName=%B3%C9%B6%BC&depCityCode=CTU&arrCityName=%C2%ED%B5%C2%C0%EF&arrCityCode=MAD&tripType=1&depDate=2018-03-31&arrDate=2018-04-07&searchBy=1281&scene=null",
               'Cookie': "orderBy=undefined; cna=JDXrEVs2YgMCAXL/oLj+ZlXF; isg=BFpa-3dt1On-IVs4fyfwKhRRqAZ1--i6J4Io02TSDe0G1_sRTRrNdcJGoyvLHFb9; enc=%2FENZJ7K1jgUPIdy2Iys91TU3vGS%2FBI2MTSRVAcPT1TpB3kK%2BLmq3KqPjTpUGKDf3SHKhT3112s3pcXbfWuk1ow%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; t=76ce689909fe34a31511b705d1a3ffe2; tracknick=chinxk; _tb_token_=taQ3UNC81Kv4GDIypOCY; cookie2=1db04fb1741b08965f8ebc12e3b9ccab",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}

    r = requests.get(url, params=params, headers=headers)
    json_text = r.text
    json_text = json_text[18:len(json_text)-2]
    json_text = json_text.replace("{0:", "{\"0\":")
    json_text = json_text.replace(",1:", ",\"1\":")
    dict_content = json.loads(json_text, encoding="utf-8")
    for flight_item in dict_content['data']['flightItems']:
        if flight_item['lowest']:
            print(flight_item['totalAdultPrice']/100)
            break

    # print(dict_content)



if __name__ == '__main__':
    get_json()
