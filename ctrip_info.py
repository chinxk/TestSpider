from bs4 import BeautifulSoup
import base_site_info
import re

class CtripInfo(base_site_info.BaseSiteInfo):

    site_name = '携程'

    def get_l_prc(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', attrs={'class': 'calendar-lowprice'})
        li = div.find('li', attrs={'class': 'tab active'})
        price = li.find('div', attrs={'class': 'price'})
        # get the middle one on the week calendar
        # self.lowest_prc = int(price.text.replace('¥', ''))
        try:
            self.lowest_prc = int(re.sub("\D", "", price.text))
        except IndexError:
            self.lowest_prc = 99999
        except ValueError:
            self.lowest_prc = 99999
        return self.lowest_prc

    def get_url(self):
        r_str = 'http://flights.ctrip.com/international/search/round-%s-%s?'
        r_str += 'depdate=%s_%s'
        r_str += '&cabin=y_s&adult=1&child=0&infant=0'
        return r_str % (self.f_city_cd, self.t_city_cd, self.f_date, self.t_date)
