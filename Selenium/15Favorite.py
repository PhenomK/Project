import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import unittest
import random

class TaskClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://172.16.52.138/user/login"

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test1(self):
        i = str(random.randint(0,10000))
        self.driver.get(self.url)
        elem1 = self.driver.find_element_by_id("user_slug")
        elem1.send_keys("chrome")                                       #用户名
        elem2 = self.driver.find_element_by_id("pwd")
        elem2.send_keys("123456")                                       #密码
        button = self.driver.find_element_by_id("submit_button")
        button.click()
        time.sleep(2)

#跳转个人文件
        elem3 = self.driver.find_element_by_link_text("个人文件")     #跳转个人文件
        elem3.click()
        time.sleep(1)
        self.driver.refresh()

        #新建收藏文件夹
        time.sleep(1)
        above = self.driver.find_element_by_id("addfile")                    #新建
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(1)
        elem4 = self.driver.find_element_by_class_name("addfolder_new")      #新建文件夹
        elem4.click()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        elem5 = self.driver.find_element_by_class_name("box")
        elem5.send_keys("selenium收藏测试文件夹"+i)
        elem6 = self.driver.find_element_by_css_selector(".sure")
        elem6.click()
        time.sleep(2)

        #勾选文件夹
        elem7 = self.driver.find_element_by_xpath("//a[@class='display-name' and @title='selenium收藏测试文件夹" + i +"']/../../../..").find_element_by_class_name("item-checkbox") #勾选文件
        elem7.click()

        #收藏
        elem8 = self.driver.find_element_by_class_name("fileMore")                                       #点击更多
        ActionChains(self.driver).move_to_element(elem8).perform()
        time.sleep(1)
        elem12 = self.driver.find_element_by_class_name("favorite")                                       #点击收藏
        elem12.click()
if __name__ == '__main__':
	unittest.main()