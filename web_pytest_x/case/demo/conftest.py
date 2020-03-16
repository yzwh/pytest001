# -*- coding:utf-8 -*- 
# user:wlx
import pytest
import allure


@allure.step("登录步骤1：输入账号")
def step1():
    print('输入账号')


@allure.step("登录步骤2：输入密码")
def step2():
    print('输入密码')


@allure.step("登录步骤3：点击登录")
def step3():
    print('点击登录按钮')


@pytest.fixture(scope='session')
def login():
    print('登录操作')

    step1()
    step2()
    step3()

