from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def get_json():
    # dcap = dict(DesiredCapabilities.PHANTOMJS)

    # 构造一个PHANTOMJS对象
    phan = dict(DesiredCapabilities.PHANTOMJS)
    # 禁止加载图片
    # phan["phantomjs.page.settings.loadImages"] = False

    # 禁用缓存
    # phan["phantomjs.page.settings.disk-cache"] = True

    phan["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)")

    phan["phantomjs.page.settings.resourceTimeout"] = 50000

    # 加载自定义配置
    browser = webdriver.PhantomJS(desired_capabilities=phan)
    browser.implicitly_wait(40000)

    browser.get("https://flight.qunar.com/site/interroundtrip_compare.htm?fromCity=%E6%88%90%E9%83%BD&toCity=%E9%A9%AC%E5%BE%B7%E9%87%8C&fromDate=2018-04-30&toDate=2018-05-07&fromCode=CTU&toCode=MAD&from=qunarindex&lowestPrice=null&isInter=true&favoriteKey=&showTotalPr=null&adultNum=1&childNum=0&cabinClass=")
    time.sleep(60)
    print(browser.page_source)
    browser.close()

    browser.quit()
if __name__ == '__main__':
    get_json()
