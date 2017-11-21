import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import random

class TaskClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://172.16.52.138/user/login"    #测试网址

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test1(self):
        i = str(random.randint(0, 10000))
        self.driver.get(self.url)
        elem1 = self.driver.find_element_by_id("user_slug")
        elem1.send_keys("chrome")                                       #用户名
        elem2 = self.driver.find_element_by_id("pwd")
        elem2.send_keys("123456")                                       #密码
        button = self.driver.find_element_by_id("submit_button")
        button.click()
        time.sleep(2)

        #跳转个人文件
        elem3 = self.driver.find_element_by_link_text("个人文件")
        elem3.click()
        time.sleep(2)
        self.driver.refresh()

        #新建文件夹
        time.sleep(2)
        above = self.driver.find_element_by_id("addfile")                    #新建
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(2)
        elem4 = self.driver.find_element_by_class_name("addfolder_new")      #新建文件夹
        elem4.click()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        elem5 = self.driver.find_element_by_class_name("box")
        elem5.send_keys("selenium文件夹"+i)
        elem6 = self.driver.find_element_by_css_selector(".sure")
        elem6.click()
        time.sleep(2)

        #新建文档
        above = self.driver.find_element_by_id("addfile")                    #新建
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(2)
        elem7 = self.driver.find_element_by_class_name("addword")#新建word文档
        time.sleep(1)
        elem7.click()
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        time.sleep(2)
        elem8 = self.driver.find_element_by_class_name("box")
        elem8.send_keys("selenium文档"+i)
        elem9 = self.driver.find_element_by_css_selector(".sure")
        elem9.click()
        time.sleep(3)

        #新建PPT
        above = self.driver.find_element_by_id("addfile")                    #新建
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(2)
        elem10 = self.driver.find_element_by_class_name("addppt")      #新建ppt
        time.sleep(1)
        elem10.click()
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        time.sleep(2)
        elem11 = self.driver.find_element_by_class_name("box")
        elem11.send_keys("selenium演示文稿"+i)
        elem12 = self.driver.find_element_by_css_selector(".sure")
        elem12.click()
        time.sleep(3)

        # 新建Excel
        above = self.driver.find_element_by_id("addfile")                    #新建
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(2)
        elem10 = self.driver.find_element_by_class_name("addexcel")#新建excel
        time.sleep(1)
        elem10.click()
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        time.sleep(2)
        elem11 = self.driver.find_element_by_class_name("box")
        elem11.send_keys("selenium表格"+i)
        elem12 = self.driver.find_element_by_css_selector(".sure")
        elem12.click()
        time.sleep(2)

if __name__ == '__main__':
	unittest.main()