from selenium import webdriver

#登陆
driver = webdriver.Chrome()
driver.get("http://172.16.52.138/user/login")
elem1 = driver.find_element_by_id("user_slug")
elem1.send_keys("chrome")
elem2 = driver.find_element_by_id("pwd")
elem2.send_keys("123456")
elem3 = driver.find_element_by_id("submit_button")
elem3.click()
