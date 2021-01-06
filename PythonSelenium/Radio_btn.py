from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radio=driver.find_elements_by_xpath("//input[@type='radio']")
print(len(radio))
radio[2].click()
assert radio[2].is_selected()