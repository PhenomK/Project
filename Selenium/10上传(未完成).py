import time
from selenium import webdriver
import os


driver = webdriver.Chrome()
driver.get("http://172.16.29.37:8080/user/login")
elem1 = driver.find_element_by_id("user_slug")
elem1.send_keys("chrome")
elem2 = driver.find_element_by_id("pwd")
elem2.send_keys("123456")
button = driver.find_element_by_id("submit_button")
button.click()
time.sleep(3)
elem3 = driver.find_element_by_link_text("个人文件")
elem3.click()
time.sleep(3)

file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)
elem4 = driver.find_element_by_class_name("uploadButton")
elem4.click()
elem4.send_keys('C:\\Users\Lenovo\Desktop\兔子.jpg')

