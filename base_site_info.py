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

    def __init__(self, msg):
        args = msg.split(',')
        self.f_city_nm = args[0]
        self.t_city_nm = args[1]
        self.f_city_cd = args[2]
        self.t_city_cd = args[3]
        self.f_date = args[4]
        self.t_date = args[5]

    @abstractmethod
    def get_l_prc(self, html):
        pass

    @abstractmethod
    def get_url(self):
        pass

    def get_dis_info(self):
        if self.lowest_prc == 99999:
            r = "站点[ %s ]失效." % self.site_name
        else:
            r = '[%s,%s],[%s]往返[%s],在[%s]上的最低价:[%s]' % (self.f_date, self.t_date, self.f_city_nm, self.t_city_nm, self.site_name, self.lowest_prc)
        return r
