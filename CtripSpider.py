import requests
import json

from selenium import webdriver


def get_json():
    url = 'http://flights.ctrip.com/international/AjaxRequest/SearchFlights/AsyncSearchHandlerSOAII.ashx'
    params = {'SearchMode': 'Search',
              'condition': '{"FlightWay":"D","SegmentList":[{"DCityCode":"CTU","ACityCode":"MAD","DCity":"Chengdu|成都(CTU)|28|CTU|480","ACity":"Madrid|马德里(MAD)|357|MAD|120","DepartDate":"2018-4-31","DCityName":"成都","ACityName":"马德里"},{"DCityCode":"MAD","ACityCode":"CTU","DCity":"Madrid|马德里(MAD)|357|MAD|480","ACity":"Chengdu|成都(CTU)|28|CTU|120","DepartDate":"2018-5-7","DCityName":"马德里","ACityName":"成都"}],"TransferCityID":0,"Quantity":1,"ClassGrade":"Y_S","TransNo":"b70dfd281f7146c3aa8b257c1b521ab3","SearchRandomKey":"","RecommendedFlightSwitch":1,"SearchKey":"6FD587833E8F51E4F796262C9AC08321A73FE6FBEC6707998AE7F2B2C8F8F677B9879539B63B903CC85FDE5F6B4DF492BD4BA71058AD3681","MultiPriceUnitSwitch":1,"TransferCitySwitch":false,"EngineScoreABTest":"A","AdjacentDateKey":"","SearchStrategySwitch":1,"MaxSearchCount":3,"TicketRemarkSwitch":1,"RowNum":"1500","TicketRemarkChannels":["GDS-WS","ZY-WS"],"AddSearchLogOneByOne":true,"TFAirlineQTE":"AA","IsWifiPackage":0,"SegmentVerifySwitch":false,"ComparePriceByAttributeSwitch":true,"IsOpenCFNoDirectRecommendYS":false,"IsDomesticIntlPUVersionSwitch":true,"DisplayBaggageSizeSwitch":true,"IsOpen24Refund":true,"IsOpenTransPU":true,"IsOpenVirtualFlight":true,"IsOpenNew3X":false,"NewAirlineLogoSwitch":false,"NewAirlineLogoSortTopSwitch":false,"IsNewImpower":false,"FromJavaVersion":false}',
              'DisplayMode': 'RoundTripGroup',
              'SearchToken': '1'}
    headers = {'Host': 'flights.ctrip.com',
               'Content-Type': "application/x-www-form-urlencoded; charset=utf-8",
               'Connection':'keep-alive',
               'Referer': 'http://flights.ctrip.com/international/round-chengdu-madrid-ctu-mad?2018-03-31&2018-04-07&y_s',
               'Cookie': "_bfa=1.1499827338101.2cam8j.1.1520602046315.1522380322858.14.23.243078; _RF1=114.255.160.184; _RSG=5zaT_b0jHW8Gd2HLsX5PbA; _RGUID=8811b409-7f76-4f45-a959-161d954429d0; _jzqco=%7C%7C%7C%7C1522380325542%7C1.270939239.1499827341046.1517820878109.1522380325332.1517820878109.1522380325332.undefined.0.0.13.13; __zpspc=9.7.1522380325.1522380325.1%231%7C%7C%7C%7C%7C%23; _ga=GA1.2.772610244.1499827341; _abtest_userid=1fd7b7bc-1ec3-4ffc-80aa-3cf094c3e50b; _RDG=28e75101dc8bb325603925f6aa8ca3e7f7; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1520602048815%7D%2C%7B%22aid%22%3A%2222347%22%2C%22timestamp%22%3A1522380325258%7D%5D; Customer=HAL=ctrip_gb; FlightIntl=Search=%5B%22Chengdu%7C%E6%88%90%E9%83%BD(CTU)%7C28%7CCTU%7C480%22%2C%22Madrid%7C%E9%A9%AC%E5%BE%B7%E9%87%8C(MAD)%7C357%7CMAD%7C60%22%2C%222018-04-21%22%2C%222018-05-01%22%5D; __utma=13090024.772610244.1499827341.1516773636.1516773636.1; __utmz=13090024.1516773636.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fpacid=09031140410925999596; GUID=09031140410925999596; Session=SmartLinkCode=U456248&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; appFloatCnt=1; Union=AllianceID=22347&SID=456248&OUID=000401app-; _bfs=1.1; adscityen=Beijing; MKT_Pagesource=PC; _bfi=p1%3D100101991%26p2%3D0%26v1%3D23%26v2%3D0; ASP.NET_SessionSvc=MTAuMTUuMTI4LjI5fDkwOTB8b3V5YW5nfGRlZmF1bHR8MTUwOTk3MDM1NDY1MQ",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}

    r = requests.post(url, data=params, headers=headers)
    json_text = r.text
    json_text = json_text[18:len(json_text) - 2]
    json_text = json_text.replace("{0:", "{\"0\":")
    json_text = json_text.replace(",1:", ",\"1\":")
    dict_content = json.loads(json_text, encoding="utf-8")
    for flight_item in dict_content['data']['flightItems']:
        if flight_item['lowest']:
            print(flight_item['totalAdultPrice'] / 100)
            break

    # print(dict_content)


if __name__ == '__main__':
    get_json()
