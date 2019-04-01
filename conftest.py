from selenium import webdriver
import pytest

global dr

@pytest.fixture(scope='session',autouse=True)
def browser():
    '''
    全局定义浏览器驱动
    :return:dr
    '''
    global dr
    dr=webdriver.Chrome()
    return dr

@pytest.fixture(scope='session',autouse=True)
def base_url():
    '''
    全局定义测试地址
    :return:url
    '''
    return "http://www.baidu.com"

@pytest.fixture(scope='session',autouse=True)
def browser_close():
    '''
    全局定义关闭浏览器
    :return:
    '''
    yield dr
    dr.quit()
    print("test end!")