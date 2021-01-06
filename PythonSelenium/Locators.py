from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# Name=driver.find_element_by_name("name")
Name=driver.find_element_by_css_selector("input[name='name']")
Name.send_keys("Abhinav Pandey")
Email=driver.find_element_by_name("email")
Email.send_keys("abhinpandey")
checkBox=driver.find_element_by_id("exampleCheck1")
checkBox.click()

submit_Btn=driver.find_element_by_xpath("//input[@type='submit']")
submit_Btn.click()

Success_test=driver.find_element_by_class_name("alert-success")
print(Success_test.text)
