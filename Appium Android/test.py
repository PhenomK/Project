#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator - Nexus_5X_API_23:5554'
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

driver.find_element_by_id("com.android.chrome:id/send_report_checkbox").click()
time.sleep(2)
driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
time.sleep(2)
driver.find_element_by_id("com.android.chrome:id/negative_button").click()
time.sleep(2)
driver.find_element_by_id("com.android.chrome:id/search_box_text").click()
time.sleep(2)
elem1 = driver.find_element_by_id("com.android.chrome:id/url_bar")
time.sleep(1)
elem1.send_keys("http://172.16.29.137/H5")
time.sleep(1)
elem2 = driver.find_element_by_class_name("android.widget.TextView")
time.sleep(1)
elem2.click()



driver.quit()