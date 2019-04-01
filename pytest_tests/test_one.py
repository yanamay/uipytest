from selenium import webdriver
import  time
def test():
    dr=webdriver.Chrome()
    dr.get("http://www.baidu.com")
'''
def test_baidu_serach(browser,base_url):
    browser.get(base_url)
    browser.implicitly_wait(10)
    browser.find_element_by_id('kw').send_keys('pytest')
    browser.find_element_by_id('su').click()
    now_time=time.strftime("%Y_%m_%d %H_%M_%S")
    print(now_time)'''

