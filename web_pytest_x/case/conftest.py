# -*- coding:utf-8 -*- 
# user:wlx
from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def driver(request):
    """定义全局driver"""
    _driver = webdriver.Chrome()
    _driver.maximize_window()

    def end():
        """测试用例完成后，执行终结函数"""
        time.sleep(4)
        _driver.quit()

    request.addfinalizer(end)
    return _driver


@pytest.fixture(scope='session')
def login(driver):
    """前置：登录"""
    web = LoginPage(driver)
    web.login()
    return driver


"""
   这个文件存放一些前置条件
"""