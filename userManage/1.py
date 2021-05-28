from Mothod_title import TestLogin
import unittest
from selenium import webdriver

class usermanage(unittest.TestCase):


    def test_Mothod(self,dr = testlogin):
        testlogin = TestLogin(self)
        dr.driver.find_element_by_link_text('员工管理').click()


    def test_Incumbency(self,dr = testlogin):
        dr.driver.find_element_by_link_text('入职登记').click()
        self.assertEqual(u'入职登记',dr.driver.title)



