# -*- coding:utf-8 -*- 
# user:wlx
import pytest


@pytest.fixture(scope='session')
def login():
    print("前置操作：登录")

    yield
    print("后置操作：关闭")


