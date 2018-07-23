from bs4 import BeautifulSoup
from urllib import parse
import base_site_info
import time
import re


class QunarInfo(base_site_info.BaseSiteInfo):

    site_name = '去哪儿'

    def get_l_prc(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(10)
        spans = soup.find_all('p', attrs={'class': 'price'})
        # get the middle one on the week calendar
        #self.lowest_prc = int(spans[3].text.replace('¥', ''))
        try:
            self.lowest_prc = int(re.sub("\D", "", spans[3].text))
        except IndexError:
            self.lowest_prc = 99999
        except ValueError:
            self.lowest_prc = 99999
        return self.lowest_prc

    def get_url(self):

        r_str = 'https://flight.qunar.com/site/interroundtrip_compare.htm?'
        r_str += 'fromCity=%s'
        r_str += '&toCity=%s'
        r_str += '&fromCode=%s'
        r_str += '&toCode=%s'
        r_str += '&fromDate=%s'
        r_str += '&toDate=%s'
        r_str += '&from=qunarindex&lowestPrice=null&isInter=true&favoriteKey=&showTotalPr=null&adultNum=1'
        r_str += '&childNum=0&cabinClass='

        return r_str % (parse.quote(self.f_city_nm), parse.quote(self.t_city_nm), self.f_city_cd, self.t_city_cd,
                        self.f_date, self.t_date)
