from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import TestSpider


def get_json():
    # 构造一个PHANTOMJS对象
    phan = dict(DesiredCapabilities.PHANTOMJS)
    # 禁止加载图片
    phan["phantomjs.page.settings.loadImages"] = False

    # 禁用缓存
    # phan["phantomjs.page.settings.disk-cache"] = True

    phan["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)")

    phan["phantomjs.page.settings.resourceTimeout"] = 50000

    # 加载自定义配置
    browser = webdriver.PhantomJS(desired_capabilities=phan)
    browser.implicitly_wait(40000)

    qunar = TestSpider.QunarInfo()
    url = qunar.get_url('成都', '马德里', 'CTU', 'MAD', '2018-05-01', '2018-05-07')
    browser.get(url)
    time.sleep(30)
    low_prc_qunar = qunar.get_l_prc(browser.page_source)
    print(low_prc_qunar)

    browser.close()
    browser.quit()


if __name__ == '__main__':
    get_json()
