import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import unittest

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
        elem1.send_keys("chrome")
        elem2 = self.driver.find_element_by_id("pwd")
        elem2.send_keys("123456")
        button = self.driver.find_element_by_id("submit_button")
        button.click()
        time.sleep(1)

        #个人文件
        elem3 = self.driver.find_element_by_link_text("个人文件")
        elem3.click()
        time.sleep(1)
        self.driver.refresh()

        #新建测试移动文件夹
        time.sleep(1)
        elem4 = self.driver.find_element_by_id("addfile")
        ActionChains(self.driver).move_to_element(elem4).perform()
        elem5 = self.driver.find_element_by_class_name("addfolder_new")
        elem5.click()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        elem6 = self.driver.find_element_by_class_name("box")
        elem6.send_keys("移动测试文件夹"+ i)
        time.sleep(1)
        elem7 = self.driver.find_element_by_css_selector(".sure")
        elem7.click()
        time.sleep(1)

        #新建测试移动文档
        time.sleep(1)
        elem8 = self.driver.find_element_by_id("addfile")
        ActionChains(self.driver).move_to_element(elem8).perform()
        time.sleep(1)
        elem9 = self.driver.find_element_by_class_name("addfolder_new")
        elem9.click()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(xoffset=400,yoffset=400).perform()
        elem10 = self.driver.find_element_by_class_name("box")
        elem10.send_keys("被移动文件夹" + i)
        time.sleep(1)
        elem11 = self.driver.find_element_by_css_selector(".sure")
        elem11.click()
        time.sleep(1)

        #勾选测试文档

        elem12 = self.driver.find_element_by_xpath("//a[@class='display-name' and @title='被移动文件夹" + i + "']/../../../..").find_element_by_class_name("item-checkbox")
        elem12.click()
        time.sleep(1)

        #移动
        elem13 = self.driver.find_element_by_class_name("fileMore")
        ActionChains(self.driver).move_to_element(elem13).perform()
        time.sleep(1)
        elem14 = self.driver.find_element_by_class_name("copy")
        elem14.click()
        time.sleep(1)
        elem15 = self.driver.find_element_by_xpath("//span[@class='jqtree-title jqtree_common' and @title='个人文件']")
        elem15.click()
        time.sleep(1)
        elem16 = self.driver.find_element_by_xpath("//span[@class='jqtree-title jqtree_common'and @title='移动测试文件夹" + i + "']")
        elem16.click()
        time.sleep(1)
        elem17 = self.driver.find_element_by_id("move-file")
        elem17.click()

if __name__ == '__main__':
	unittest.main()


