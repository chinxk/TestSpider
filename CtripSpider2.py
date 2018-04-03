from selenium import webdriver


def get_json():
    browser = webdriver.Firefox()
    browser.get("https://www.qunar.com/")
    input_str = browser.find_element_by_id('q')
    input_str.clear()
    input_str.send_keys("MakBook pro")
    button = browser.find_element_by_class_name('btn-search')
    button.click()
    print(browser.page_source)


if __name__ == '__main__':
    get_json()
