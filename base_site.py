from abc import ABCMeta, abstractmethod


class BaseSite:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_l_prc(self, html):
        pass

    @abstractmethod
    def get_url(self):
        pass
