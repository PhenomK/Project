import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

#登陆
driver = webdriver.Chrome()
driver.get("http://172.16.29.71/user/login")           #测试网址
elem1 = driver.find_element_by_id("user_slug")
elem1.send_keys("chrome")                                       #用户名
elem2 = driver.find_element_by_id("pwd")
elem2.send_keys("123456")                                       #密码
button = driver.find_element_by_id("submit_button")
button.click()
time.sleep(2)

#跳转个人文件
elem3 = driver.find_element_by_link_text("个人文件")
elem3.click()
time.sleep(1)
driver.refresh()

#新建文件夹
time.sleep(1)
above = driver.find_element_by_id("addfile")                    #新建
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
elem4 = driver.find_element_by_class_name("addfolder_new")      #新建文件夹
elem4.click()
time.sleep(1)
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
elem5 = driver.find_element_by_class_name("box")
elem5.send_keys("selenium文件夹")
elem6 = driver.find_element_by_css_selector(".sure")
elem6.click()
time.sleep(2)

#新建文档
above = driver.find_element_by_id("addfile")                    #新建
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
elem7 = driver.find_element_by_class_name("addword")#新建word文档
time.sleep(0.5)
elem7.click()
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
time.sleep(1)
elem8 = driver.find_element_by_class_name("box")
elem8.send_keys("selenium文档")
elem9 = driver.find_element_by_css_selector(".sure")
elem9.click()
time.sleep(3)

#新建PPT
above = driver.find_element_by_id("addfile")                    #新建
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
elem10 = driver.find_element_by_class_name("addppt")      #新建ppt
time.sleep(0.5)
elem10.click()
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
time.sleep(1)
elem11 = driver.find_element_by_class_name("box")
elem11.send_keys("selenium演示文稿")
elem12 = driver.find_element_by_css_selector(".sure")
elem12.click()
time.sleep(3)

# 新建Excel
above = driver.find_element_by_id("addfile")                    #新建
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
elem10 = driver.find_element_by_class_name("addexcel")#新建excel
time.sleep(0.5)
elem10.click()
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
time.sleep(1)
elem11 = driver.find_element_by_class_name("box")
elem11.send_keys("selenium表格")
elem12 = driver.find_element_by_css_selector(".sure")
elem12.click()
time.sleep(1)