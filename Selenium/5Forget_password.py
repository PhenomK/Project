import  unittest
from selenium import webdriver
import time

class TaskClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://172.16.52.138/user/login"

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test1(self):
        self.driver.get(self.url)
        elem1 = self.driver.find_element_by_class_name("forgot_password_text")
        elem1.click()

if __name__ == '__main__':
	unittest.main()
