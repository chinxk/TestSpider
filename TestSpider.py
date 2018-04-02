import requests
import json
# 这里使用requests，小脚本用它最合适！

def get_json():
    # url = 'https://flight.qunar.com/twell/flight/inter/search?depCity=成都&arrCity=马德里&depDate=2018-03-30&retDate=2018-04-19&adultNum=1&childNum=0&ex_track=&from=qunarindex&queryId=10.90.53.108:l:1d794bc1:1626843613d:41f0&es=PjQ1xJ13tFyMcC137tyPxCykEbehcJ1kE6ePi6JZJehhrJv8Mb======|1522203389663'
    url = 'https://flight.qunar.com/twell/flight/inter/search'
    params = {'depCity': '成都',
              'arrCity': '马德里',
              'depDate': '2018-04-01',
              'adultNum': '1',
              'childNum': '0',
              'from': 'qunarindex',
              'ex_track': '',
              'es': 'todo',
              'queryId': '10.90.53.108:l:-23935a05:1626d0b62fa:71ff',
              'retDate': '2018-04-07'}
    ess = ['yPOQLOKQypBIkZxoIU7I3jxQypsIPj0/yp7Qpj/gLTP0fj/gy3======|1522286311077',
           'yPOQkOxsyjeQcOxQIU7I3jxQypsIPj0/yp7Qpj/gLTP0fj3gy3======|1522286311077',
           'yPOQ3OKLljBIyOxLIU7I3jxQypsIPj0/yp7Qpj/gLTP0fO/gy3======|1522286311077',
           'yPOQ3j0slpBIpjK7IU7I3jxQypsIPj0/yp7Qpj/gLTP0fj4gy3======|1522286311077',
           'yPOQ/j7olPUIyZ0kIU7I3jxQypsIPj0/yp7Qpj/gLTP0fOPgy3======|1522286311077',
           'yPOQkj7Bl3BIPj07IUsIjZ0oIf03cl7/IU7P====|1522286311077']


    headers = {'Host': "flight.qunar.com",
               'Cookie': "QN1=ezu0oVmWh1llHStmRvHjAg==; QN99=4604; QunarGlobal=192.168.31.93_5c75abef_15e5b93e851_3a22|1504776613365; QN601=3c74f114ee186a9e21647fad66429d82; _i=RBTKA8mux8TxVyPRsJgt1QxhrITx; _vi=NT_g90knVGNheRAOJa2kXRD6OL4uAu9GRURDxLjTuOWD5pALpK84qRKNANjr_qByLVYXKrsuBs_OqNc33HzYAzstrstbyvPERYCqpaluaeOGdLrO3bfu8KmIGfJfMNwfKX6A8rS28gO8tISw7zwIPqi1hvkBOk8gpLbuKPxxi8OD; Hm_lvt_75154a8409c0f82ecd97d538ff0ab3f3=1522205272; QN48=tc_9f3373ab0f7c0b76_15e5bacf6ac_6b1b; QN621=1490067914133%3DDEFAULT%26fr%3Dqunarindex; QN170=106.38.0.104_a21153_0_xi1hBqP0dhVMgV5FUrhFDfHS%2Bp5gNbMj00MpYF5oAv8%3D; QN171=linktechID|A10004265310278697|2492991986012D^20170526183959-86580|99999|01; SplitEnv=D; ag_fid=AJWwsIADF9J9nEXF; QN269=BB175A0066AB11E78CF4FA163E620FF6; QN205=organic; QN277=organic; csrfToken=5ygcVZnczyUxFpXBogPNqDbdFrb22tRw; QN163=0; PHPSESSID=ll4bsqk09a4m2185qa31rkqbb3; Hm_lpvt_75154a8409c0f82ecd97d538ff0ab3f3=1522205272",
               'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0"}
    lowest_price = 99999

    for es in ess:
        params['es'] = es
        r = requests.get(url, params=params, headers=headers)
        dict_content = json.loads(r.text, encoding="gb2312")
        # print(dict_content)
        flight_prices = dict_content['result']['flightPrices']
        # print(flight_prices)
        for key in flight_prices:
            if lowest_price > flight_prices[key]['price']['lowTotalPrice']:
                lowest_price = flight_prices[key]['price']['lowTotalPrice']
            print(key, flight_prices[key]['price']['lowTotalPrice'])

    print(lowest_price)


if __name__ == '__main__':
    get_json()
