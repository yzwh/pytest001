# -*- coding:utf-8 -*- 
# user:wlx

import yaml
import os


def readyml(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    y = f.read()
    data = yaml.load(y, Loader=yaml.FullLoader)
    print("读取yaml转字典:%s" % data)
    return data


if __name__ == '__main__':
    a = readyml(r'G:\2020\web_pytest_x\case\testdata.yml')
    print(a['test_sum_data'])


