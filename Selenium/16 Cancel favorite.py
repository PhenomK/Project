import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

#登陆
driver = webdriver.Chrome()
driver.get("http://172.16.52.138/user/login")
elem1 = driver.find_element_by_id("user_slug")
elem1.send_keys("chrome")
elem2 = driver.find_element_by_id("pwd")
elem2.send_keys("123456")
button = driver.find_element_by_id("submit_button")
button.click()
time.sleep(1)

#个人文件
elem3 = driver.find_element_by_link_text("个人文件")
elem3.click()
time.sleep(1)
driver.refresh()

#取消收藏文件夹
time.sleep(1)
elem4 = driver.find_element_by_xpath("//a[@class='display-name' and @title='selenium收藏测试文件夹']/../../../..").find_element_by_class_name("item-checkbox")
elem4.click()
time.sleep(1)
elem5 = driver.find_element_by_class_name("fileMore")
ActionChains(driver).move_to_element(elem5).perform()
time.sleep(1)
elem6 = driver.find_element_by_xpath("//span[@class='cancelfavorite cancelfavorite-true']")
elem6.click()

#我的收藏
time.sleep(1)
elem7 = driver.find_element_by_link_text("我的收藏")
elem7.click()