from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://172.16.29.71/user/login")
elem1 = driver.find_element_by_class_name("forgot_password_text")
elem1.click()
