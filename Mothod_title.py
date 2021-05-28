# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,re,time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.ctgpayroll.com/www/index.html')
        self.verificationErrors = []
        driver = self.driver
        driver.find_element_by_link_text('企业登录').click()
        # 获得打开的第一个窗口句柄
        window_1 = driver.current_window_handle
        # 获得打开的所有的窗口句柄
        windows = driver.window_handles
        # 切换到最新的窗口
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
        driver.find_element_by_name('mobile').send_keys('18612533709')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_class_name('register-btn').click()

    def testIndex_title(self):
        #登录成功验证首页title
        driver = self.driver
        self.assertEqual(u'首页-易HR企业端',driver.title)

    def test_Workbench(self):
        driver = self.driver
        driver.find_element_by_link_text('组织结构').click()
        self.assertEqual(u'组织结构',driver.title)

    def test_Organization (self):
        driver = self.driver
        driver.find_element_by_link_text('工作台').click()
        self.assertEqual(u'工作台', driver.title)

    def test_Usermanage(self):
        driver = self.driver
        driver.find_element_by_link_text('员工管理').click()
        self.assertEqual(u'在职员工', driver.title)

    def test_Salary(self):
        driver = self.driver
        driver.find_element_by_link_text('薪酬管理').click()
        self.assertEqual(u'薪酬管理', driver.title)

    def test_Socialsecurity(self):
        driver = self.driver
        driver.find_element_by_link_text('社保管理').click()
        self.assertEqual(u'社保管理', driver.title)

    def test_Daily(self):
        driver = self.driver
        driver.find_element_by_link_text('考勤管理').click()
        self.assertEqual(u'考勤管理', driver.title)

    def test_Approval(self):
        driver = self.driver
        driver.find_element_by_link_text('审批管理').click()
        self.assertEqual(u'审批', driver.title)

    def test_Notice(self):
        driver = self.driver
        driver.find_element_by_link_text('公告').click()
        self.assertEqual(u'公告', driver.title)

    def test_Setup(self):
        driver = self.driver
        driver.find_element_by_link_text('设置').click()
        self.assertEqual(u'账号设置', driver.title)
        alert = driver.switch_to_alert()
        self.assertEqual(u'保存成功',alert.text)

    def test_Reportcenter(self):
        driver = self.driver
        driver.find_element_by_link_text('报表中心').click()
        self.assertEqual(u'报表管理', driver.title)

    def test_Merchant(self):
        driver = self.driver
        driver.find_element_by_link_text('商保管理').click()
        self.assertEqual(u'商保管理', driver.title)

    def test_Payroll(self):
        driver = self.driver
        driver.find_element_by_link_text('工资单').click()
        self.assertEqual(u'工资单', driver.title)

    def test_Contract(self):
        driver = self.driver
        driver.find_element_by_link_text('合同管理').click()
        self.assertEqual(u'合同签订', driver.title)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()


