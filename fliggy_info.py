from bs4 import BeautifulSoup
from urllib import parse
import base_site_info
import re
import time


class FliggyInfo(base_site_info.BaseSiteInfo):

    site_name = '飞猪'

    def get_l_prc(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(10)
        try:
            div = soup.find('div', attrs={'class': 'week-price'})
            td = div.find('td', attrs={'class': 'current'})
            price = td.find('span', attrs={'class': 'totalprice'})
            #self.lowest_prc = int(price.text.replace('¥', ''))
            self.lowest_prc = int(re.sub("\D", "", price.text))
        except AttributeError:
            self.lowest_prc = 99999
        except IndexError:
            self.lowest_prc = 99999
        except ValueError:
            self.lowest_prc = 99999
        return self.lowest_prc

    def get_url(self):
        r_str = 'https://sijipiao.fliggy.com/ie/flight_search_result.htm?tripType=1'
        r_str += '&depCityName=%s'
        r_str += '&arrCityName=%s'
        r_str += '&depCity=%s'
        r_str += '&arrCity=%s'
        r_str += '&depDate=%s'
        r_str += '&arrDate=%s'

        return r_str % (parse.quote(self.f_city_nm), parse.quote(self.t_city_nm), self.f_city_cd,
                        self.t_city_cd, self.f_date, self.t_date)
