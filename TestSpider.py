from bs4 import BeautifulSoup
from urllib import parse
import base_site


class QunarInfo(base_site.BaseSite):

    def get_l_prc(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        spans = soup.find_all('p', attrs={'class': 'price'})
        print(spans[3].text)
        return spans[3].text.replace('¥', '')

    def get_url(self, f_city_nm, t_city_nm, f_city_cd, t_city_cd, f_date, t_date):

        r_str = 'https://flight.qunar.com/site/interroundtrip_compare.htm?'
        r_str += 'fromCity=%s'
        r_str += '&toCity=%s'
        r_str += '&fromCode=%s'
        r_str += '&toCode=%s'
        r_str += '&fromDate=%s'
        r_str += '&toDate=%s'
        r_str += '&from=qunarindex&lowestPrice=null&isInter=true&favoriteKey=&showTotalPr=null&adultNum=1'
        r_str += '&childNum=0&cabinClass='

        return r_str % (parse.quote(f_city_nm), parse.quote(t_city_nm), f_city_cd, t_city_cd, f_date, t_date)
