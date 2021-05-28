from  selenium import webdriver
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://47.92.110.143/www/index.html')
driver.find_element_by_link_text('企业登录').click()
# time.sleep(2000)
#获得打开的第一个窗口句柄
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
