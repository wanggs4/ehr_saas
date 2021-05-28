# -*- coding: utf-8 -*-
import re
from selenium import webdriver
import unittest,re,time

class TestLogin(unittest.TestCase):

    def setUp(self):
        print('open')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.ctgpayroll.com/www/index.html')
        self.verificationErrors = []
        # 获得打开的第一个窗口句柄
        window_1 = driver.current_window_handle
        # 获得打开的所有的窗口句柄
        windows = driver.window_handles
        # 切换到最新的窗口
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
        driver.find_element_by_link_text('企业登录').click()
        driver.find_element_by_name('mobile').send_keys('18612533709')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_class_name('register-btn').click()

    def testlogin_index(self):
        driver = self.driver
        TestLogin.setUp()
        self.assertEqual('','')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()


