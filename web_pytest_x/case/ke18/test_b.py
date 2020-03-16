# -*- coding:utf-8 -*- 
# user:wlx

import pytest


def test_1(login):
    print("测试用例111")


def test_2(login):
    print("测试用例222")
    assert 1==2


def test_3(login):
    print("测试用例333")




"""
count默认重复用例
要重复执行整个会话的话要加个参数  --repeat-scope=[session,function等值]，与 fixure的scope类似
"""