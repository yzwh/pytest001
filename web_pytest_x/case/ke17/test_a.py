# -*- coding:utf-8 -*- 
# user:wlx

import pytest
from common.read_yml import readyml
import os

curpath = os.path.dirname(os.path.dirname(__file__))

a = readyml(os.path.join(curpath, "testdata.yml"))

# a = readyml(r'G:\2020\web_pytest_x\case\testdata.yml')
testdata = a['test_sum_data']


@pytest.mark.parametrize("test_input, expected", testdata)
# @pytest.mark.test1
def test_demo(test_input, expected):
    a = test_input
    assert eval(a) == expected


@pytest.mark.parametrize("test_input, expected",
                         [["1+2", 3],
                          ["2*3", 6],
                          ["3-7", -4]])
# @pytest.mark.skip(reason="测试跳过")
# @pytest.mark.test2
def test_demo2(test_input, expected):
    a = test_input
    assert eval(a) == expected

