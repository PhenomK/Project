from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://172.16.29.71/user/login")
elem1 = driver.find_element_by_class_name("login_language")
elem1.click()
time.sleep(2)
elem2 = driver.find_element_by_class_name("login_language")
elem2.click()
