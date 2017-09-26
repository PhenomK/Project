from selenium import webdriver
import time

#登陆
driver = webdriver.Chrome()
driver.get("http://172.16.29.71/user/login")
elem1 = driver.find_element_by_id("user_slug")
elem1.send_keys("chrome")
elem2 = driver.find_element_by_id("pwd")
elem2.send_keys("123456")
elem3 = driver.find_element_by_id("submit_button")
elem3.click()
time.sleep(1)

#退出
elem4 = driver.find_element_by_link_text("退出")
elem4.click()