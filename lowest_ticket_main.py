from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import qunar_info
import ctrip_info
import fliggy_info
import skyscanner_info
import email_sender
import base_site_info

def get_site_lowest_site(target_sites):
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

    current_price = 99999
    lowest_site = base_site_info.BaseSiteInfo('', '', '', '', '', '')
    for site in target_sites:
        url = site.get_url()
        browser.get(url)
        time.sleep(10)
        prc = site.get_l_prc(browser.page_source)
        if prc < current_price:
            current_price = prc
            lowest_site = site
        print(site.get_dis_info())

    browser.close()
    browser.quit()
    return lowest_site


if __name__ == '__main__':

    eml_pw = input("email password : = ")
    tgt_prc = int(input("target price : = "))

    qunar = qunar_info.QunarInfo('成都', '马德里', 'CTU', 'MAD', '2018-05-01', '2018-05-07')
    ctrip = ctrip_info.CtripInfo('成都', '马德里', 'CTU', 'MAD', '2018-05-01', '2018-05-07')
    fliggy = fliggy_info.FliggyInfo('成都', '马德里', 'CTU', 'MAD', '2018-05-01', '2018-05-07')
    skyscanner = skyscanner_info.SkyScannerInfo('成都', '马德里', 'CTU', 'MAD', '2018-05-01', '2018-05-07')

    target_sites = [qunar, ctrip, fliggy, skyscanner]
    target_site = get_site_lowest_site(target_sites)

    if target_site.lowest_prc < tgt_prc:
        print("目前价格%s,低于预设最低价格%s.开始Email通知." % (target_site.lowest_prc, tgt_prc))
        email_sender.sent_email(eml_pw, target_site.get_dis_info())
