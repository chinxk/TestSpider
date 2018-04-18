import requests
import json


def get_json(dep_city_code, arr_city_code, dep_date, dep_date2):
    url = 'https://sijipiao.fliggy.com/ie/flight_search_result_poller.do'
    params = {'supportMultiTrip': 'true',
              'searchBy': '1281',
              #'searchJourney': '[{"depCityCode":"CTU","arrCityCode":"MAD","depCityName":"","arrCityName":"","depDate":"2018-04-31","selectedFlights":[]},{"depCityCode":"MAD","arrCityCode":"CTU","arrCityName":"","depCityName":"","depDate":"2018-05-07","selectedFlights":[]}]',
              'searchJourney': '[{"depCityCode":"%s","arrCityCode":"%s","depCityName":"","arrCityName":"","depDate":"%s","selectedFlights":[]},{"depCityCode":"%s","arrCityCode":"%s","arrCityName":"","depCityName":"","depDate":"%s","selectedFlights":[]}]'%(dep_city_code, arr_city_code, dep_date, arr_city_code, dep_city_code, dep_date2),
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
               'Cookie': "orderBy=undefined; cna=JDXrEVs2YgMCAXL/oLj+ZlXF; isg=BFpa-3dt1On-IVs4fyfwKhRRqAZ1--i6J4Io02TSDe0G1_sRTRrNdcJGoyvLHFb9; enc=%2FENZJ7K1jgUPIdy2Iys91TU3vGS%2FBI2MTSRVAcPT1TpB3kK%2BLmq3KqPjTpUGKDf3SHKhT3112s3pcXbfWuk1ow%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; t=76ce689909fe34a31511b705d1a3ffe2; tracknick=chinxk; _tb_token_=taQ3UNC81Kv4GDIypOCY; cookie2=1db04fb1741b08965f8ebc12e3b9ccab",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}

    r = requests.get(url, params=params, headers=headers)
    json_text = r.text
    # print(json_text)
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
    get_json('CTU', 'MAD', '2018-04-30', '2018-05-07')
