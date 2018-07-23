from bs4 import BeautifulSoup
import base_site_info
import re


class SkyScannerInfo(base_site_info.BaseSiteInfo):

    site_name = '天巡国际'

    def get_l_prc(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        spans = soup.find_all('span', attrs={'class': 'fqs-price'})
        # get the middle one on the fqs ops
        # self.lowest_prc = int(spans[1].text.replace('¥', '').replace(',', ''))
        try:
            self.lowest_prc = int(re.sub("\D", "", spans[1].text))
        except IndexError:
            self.lowest_prc = 99999
        except ValueError:
            self.lowest_prc = 99999

        return self.lowest_prc

    def get_url(self):
        r_str = 'https://www.skyscanner.net/transport/flights/%s/%s/%s/%s'
        r_str += '?adults=1&children=0&rtn=1&currency=CNY'
        f_date = self.f_date.replace('-', '')[2:8]
        t_date = self.t_date.replace('-', '')[2:8]
        return r_str % (self.f_city_cd, self. t_city_cd, f_date, t_date)
