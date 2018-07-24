from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import qunar_info
import ctrip_info
import fliggy_info
import skyscanner_info
import email_sender
import base_site_info
import redis


def deal_msg(msg):
    qunar = qunar_info.QunarInfo(msg)
    ctrip = ctrip_info.CtripInfo(msg)
    fliggy = fliggy_info.FliggyInfo(msg)
    skyscanner = skyscanner_info.SkyScannerInfo(msg)

    target_sites = [qunar, ctrip, fliggy, skyscanner]
    # target_sites = [skyscanner]
    target_site = get_site_lowest_site(target_sites)

    if target_site.lowest_prc < tgt_prc:
        print("目前最低价格%s,低于预设最低价格%s.开始Email通知." % (target_site.lowest_prc, tgt_prc))
    # email_sender.sent_email(eml_pw, target_site.get_dis_info())


class SampleListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        print('received a message %s' % message)
        deal_msg(message)


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
    lowest_site = base_site_info.BaseSiteInfo(',,,,,')
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

    #eml_pw = input("email password : = ")
    tgt_prc = int(input("target price : = "))

    #read mq
    #conn = stomp.Connection(host_and_ports=[('localhost', '61613')])
    #conn.set_listener("", SampleListener())
    #conn.start()
    #conn.connect(login='admin', password='admin')
    #conn.subscribe(destination='/queue/test', id=3, ack='auto')
    #print("waiting for messages...")
    #while 1:
    #    time.sleep(10)

    # read redis
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, password='rd123467')
    r = redis.StrictRedis(connection_pool=pool)

    while 1:
        keys = r.keys()
        print(keys)
        for key in keys:
            msg = r.get(key).decode('gbk')
            print('msg:%s' % msg)
            deal_msg(msg)

    #msg = '成都,新加坡,CTU,SIN,2018-12-15,2018-12-19'
    #conn.send(body=msg, destination='/queue/test')
    #time.sleep(2)
    #conn.disconnect()


