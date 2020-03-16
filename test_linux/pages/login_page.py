# -*- coding:utf-8 -*- 
# user:wlx

from common.base import Base
from common.config import host
import pytest


login_url = host+'/lds/'


class LoginPage(Base):
    """登录页面"""
    # 定位元素（属性）
    loc1 = ('id', 'username')
    loc2 = ('id', 'password')
    loc3 = ('id', 'login-Button')

    loc4 = ('xpath', '/html/body/div/div[1]/div[2]/div/div[1]')

    def input_user(self, username):
        self.send_values(self.loc1, username)

    def input_psw(self, psw):
        self.send_values(self.loc2, psw)

    def click_btn(self):
        self.click(self.loc3)

    def login(self, username='黄晓慧', psw='123456'):
        self.driver.get(login_url)
        self.input_user(username)
        self.input_psw(psw)
        self.click_btn()

    # 判断是否登录成功
    def is_login_success(self):
        """判断是否登录成功，返回布尔值"""
        text = self.get_text(self.loc4)
        print("登录完成后，获取页面文本元素：%s" % text)
        return text == '数字监管'


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    # driver.get("http://192.168.90.161:8080/lds/")
    web.login()

    # 断言
    result = web.is_login_success()
    print(result)
    assert result
    driver.quit()
