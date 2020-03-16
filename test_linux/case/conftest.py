
# -*- coding:utf-8 -*-
# user:wlx
from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import platform
print(platform.system())


@pytest.fixture(scope='session')
def driver(request):
    """定义全局driver"""
    if platform.system() == 'windows':
        _driver = webdriver.Chrome()
    else:
        # 启动Linux
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无界面
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度

        _driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
    # _driver = webdriver.Chrome()
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


