# -*- coding:utf-8 -*- 
# user:wlx

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os

timeout = 30
t = 0.5


class Base1(object):
    # def __init__(self, driver):
    #     self.driver = driver
    #     self.timeout = 30
    #     self.t = 0.5

    # 定位元素方法，返回定位到的元素
    def find_element(self, locator):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须是元组类型：loc=('xpath','value')")
        else:
            try:
                print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
                ele = WebDriverWait(self.driver, timeout, t).until(EC.presence_of_element_located(locator))
                return ele
            except:
                return []

    # 定位元素的另一种方法(lambda中的x相当于driver)
    def find_element_1(self, locator):
        try:
            ele = WebDriverWait(self.driver, timeout, t).until(lambda x: x.find_element(*locator))
            return ele
        except:
            return []

    # 定位元素集方法，返回定位到的一组元素
    def find_elements(self, locator):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须是元组类型：loc=('id','value')")
        else:
            try:
                print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
                eles = WebDriverWait(self.driver, timeout, t).until(EC.presence_of_element_located(locator))
                return eles
            except:
                return []

    # 判断当前页面title是否等于预期,返回布尔值
    def is_title_equals(self, _title):
        try:
            r = WebDriverWait(self.driver, timeout, t).until(EC.title_is(_title))
            return r
        except:
            return False

    # 判断当前页面title是否包含某值，返回布尔值
    def is_title_contains(self, _title):
        try:
            r = WebDriverWait(self.driver, timeout, t).until(EC.title_contains(_title))
            return r
        except:
            return False

    # 判断某个元素中的text是否包含了预期的字符串，返回布尔值
    def is_ele_text_contains(self, locator, _text):
        try:
            r = WebDriverWait(self.driver, timeout, t).until(EC.text_to_be_present_in_element(locator, _text))
            return r
        except:
            return False

    # 判断某个元素中的value属性是否包含预期的字符串，返回布尔值
    def is_ele_value_contains(self, locator, _text):
        try:
            r = WebDriverWait(self.driver, timeout, t).until(EC.text_to_be_present_in_element_value(locator, _text))
            return r
        except:
            return False

    # 判断元素是否存在，返回布尔值
    def ele_is_exist(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    # 判断元素是否存在(另一种写法)
    def eles_is_exist(self, locator):
        eles = self.find_elements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print('定位到的元素个数为：%s' % n)
            return True

    # 判断页面上弹框是否存在(如果存在则返回alert弹框)
    def is_alert_exist(self):
        try:
            r = WebDriverWait(self.driver, timeout, t).until(EC.alert_is_present())
            return r
        except:
            return False

    # 获取页面title
    def get_title(self):
        return self.driver.title

    # 获取元素文本
    def get_text(self, locator):
        try:
            ele = self.find_element(locator)
            text = ele.text
            return text
        except:
            print("获取元素文本失败，返回空")
            return ''

    # 输入内容方法
    def send_values(self, locator, _text):
        ele = self.find_element(locator)
        ele.send_keys(_text)

    # 清空方法
    def clear(self, locator):
        ele = self.find_element(locator)
        ele.clear()

    # 元素点击方法
    def click(self, locator):
        ele = self.find_element(locator)
        ele.click()

    # 判断元素是否被选中,返回布尔值
    def selected_or_not(self, locator):
        ele = self.find_element(locator)
        b = ele.is_selected()
        print(b)
        # return b

    # 退出浏览器
    def quit_browser(self):
        self.driver.quit()

    # 鼠标悬停方法，避免每次都要导入鼠标事件的模块
    def move_to_ele(self, locator):
        ele = self.find_element(locator)
        ActionChains(driver).move_to_element(ele).perform()

    # 通过索引定位select，从0开始，默认选中第一个
    def select_by_index(self, locator, index=0):
        # 定位到select这一栏
        ele = self.find_element(locator)
        Select(ele).select_by_index(index)

    # 通过value属性定位select
    def select_by_value(self, locator, value):
        ele = self.find_element(locator)
        Select(ele).select_by_value(value)

    # 通过文本值定位select
    def select_by_text(self, locator, text):
        ele = self.find_element(locator)
        Select(ele).deselect_by_visible_text(text)

    # 滚动到窗口顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.excute_script(js)

    # 滚动到窗口底部
    def js_scroll_end(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    # 横向滚动(以参数形式就好了)
    def js_scroll_x(self, x):
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)

    # 聚焦元素
    def js_focus_ele(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 切换iframe
    def exchange_frame(self, loc):
        ele = self.find_element(loc)
        self.driver.switch_to.frame(ele)


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://192.168.90.161:8080/lds/')
    # 创建类的对象
    lds = Base1(driver)

    # 第一种定位方法,用于find_element方法
    # loc1 = (By.ID, 'account')
    # loc2 = (By.NAME, 'password')
    # loc3 = (By.ID, 'submit')

    loc1 = ('id', 'username')
    loc2 = ('id', 'password')
    loc3 = ('xpath', '//div[@id="select-org"]/span')
    loc4 = ('id', 'autoLogin')

    lds.send_values(loc1, '黄晓慧')
    lds.send_values(loc2, '123456')

    lds.selected_or_not(loc4)
    lds.quit_browser()


