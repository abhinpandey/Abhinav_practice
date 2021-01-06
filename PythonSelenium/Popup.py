from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
popup_text=driver.find_element_by_id("name")
name="Abhinav"
popup_text.send_keys(name)
popup=driver.find_element_by_id("alertbtn")
popup.click()
print()
alert=driver.switch_to.alert
alertText=alert.text
assert  name in alertText
print(alert.text)
alert.accept()