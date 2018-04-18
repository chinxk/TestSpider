from abc import ABCMeta, abstractmethod


class BaseSiteInfo:
    __metaclass__ = ABCMeta

    site_name = 'BASE'
    lowest_prc: int = -1
    f_city_nm = 'null'
    t_city_nm = 'null'
    f_city_cd = 'null'
    t_city_cd = 'null'
    f_date = 'null'
    t_date = 'null'

    def __init__(self, f_city_nm, t_city_nm, f_city_cd, t_city_cd, f_date, t_date):
        self.f_city_nm = f_city_nm
        self.t_city_nm = t_city_nm
        self.f_city_cd = f_city_cd
        self.t_city_cd = t_city_cd
        self.f_date = f_date
        self.t_date = t_date

    @abstractmethod
    def get_l_prc(self, html):
        pass

    @abstractmethod
    def get_url(self):
        pass

    def get_dis_info(self):
        return '[%s,%s],[%s]往返[%s],在[%s]上的最低价:[%s]' % (self.f_date, self.t_date, self.f_city_nm, self.t_city_nm, self.site_name, self.lowest_prc)
