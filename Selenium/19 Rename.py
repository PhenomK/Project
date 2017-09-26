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
elem5.send_keys("selenium重命名文件夹")
elem6 = driver.find_element_by_css_selector(".sure")
elem6.click()
time.sleep(2)

#重命名
elem7 = driver.find_element_by_xpath("//a[@class='display-name' and @title='selenium重命名文件夹']/../../../..").find_element_by_class_name("item-checkbox")
elem7.click()
time.sleep(1)
elem8 = driver.find_element_by_class_name("fileMore")
ActionChains(driver).move_to_element(elem8).perform()
time.sleep(1)
elem9 = driver.find_element_by_class_name("rename")
elem9.click()
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
time.sleep(1)
elem10 = driver.find_element_by_class_name("rename-input")
elem10.send_keys("selenium二次重命名文件夹")
elem11 = driver.find_element_by_css_selector(".sure")
elem11.click()
