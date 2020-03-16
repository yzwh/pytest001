# -*- coding:utf-8 -*- 
# user:wlx
import pytest
from pages.add_article_page import AddArticle
import allure


@allure.feature("文章分类")
class TestArticle():

    @allure.title("编辑文章分类，输入数据，编辑成功")
    @allure.testcase("禅道或jira上测试用例地址")
    # login 是前置条件 conftest中定义的
    def test_add_article1(self, login):
        """用例描述（相当于禅道中的用例步骤）"""
        driver = login

    @allure.title("编辑文章分类，输入数据，编辑成功")
    @allure.testcase("禅道或jira上测试用例地址")
    @allure.issue("用例关联的bug地址[该条用例执行失败会记录bug，就是那个bug地址]")
    def test_add_article2(self, login):
        """用例描述（相当于禅道中的用例步骤）"""
        driver = login
