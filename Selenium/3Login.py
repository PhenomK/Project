import unittest
from selenium import webdriver
import time

#登陆
class TaskClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://172.16.52.138/user/login"

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test1(self):
        self.driver.get(self.url)
        elem1 = self.driver.find_element_by_id("user_slug")
        elem1.send_keys("chrome")
        elem2 = self.driver.find_element_by_id("pwd")
        elem2.send_keys("123456")
        elem3 = self.driver.find_element_by_id("submit_button")
        elem3.click()

if __name__ == '__main__':
	unittest.main()