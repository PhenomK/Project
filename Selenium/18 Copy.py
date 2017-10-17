import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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

#新建测试移动文件夹
time.sleep(1)
elem4 = driver.find_element_by_id("addfile")
ActionChains(driver).move_to_element(elem4).perform()
elem5 = driver.find_element_by_class_name("addfolder_new")
elem5.click()
time.sleep(1)
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
elem6 = driver.find_element_by_class_name("box")
elem6.send_keys("复制测试文件夹")
time.sleep(1)
elem7 = driver.find_element_by_css_selector(".sure")
elem7.click()
time.sleep(1)

#新建测试移动文档
time.sleep(1)
elem8 = driver.find_element_by_id("addfile")
ActionChains(driver).move_to_element(elem8).perform()
time.sleep(1)
elem9 = driver.find_element_by_class_name("addword")
elem9.click()
time.sleep(1)
ActionChains(driver).move_by_offset(xoffset=400,yoffset=400).perform()
elem10 = driver.find_element_by_class_name("box")
elem10.send_keys("复制测试文档")
time.sleep(1)
elem11 = driver.find_element_by_css_selector(".sure")
elem11.click()
time.sleep(1)

#勾选测试文档
elem12 = driver.find_element_by_xpath("//a[@class='display-name' and @title='复制测试文档.docx']/../../../..").find_element_by_class_name("item-checkbox")
elem12.click()
time.sleep(1)

#复制
elem13 = driver.find_element_by_class_name("fileMore")
ActionChains(driver).move_to_element(elem13).perform()
time.sleep(1)
elem14 = driver.find_element_by_class_name("copy")
elem14.click()
time.sleep(1)
elem15 = driver.find_element_by_xpath("//span[@class='jqtree-title jqtree_common' and @title='个人文件']")
elem15.click()
time.sleep(1)
elem16 = driver.find_element_by_xpath("//span[@class='jqtree-title jqtree_common'and @title='复制测试文件夹']")
elem16.click()
time.sleep(1)
elem17 = driver.find_element_by_id("copy-file")
elem17.click()