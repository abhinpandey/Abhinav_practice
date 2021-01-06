from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/")
# Login=driver.find_element_by_css_selector("input#username")
Name=driver.find_element_by_css_selector("input#username")
Name.send_keys("Abhinav Pandey")

password=driver.find_element_by_css_selector(".password")
password.send_keys("Abhinpandey")
password.clear()

forget_password=driver.find_element_by_link_text("Forgot Your Password?")
forget_password.click()

Cancel_btn=driver.find_element_by_xpath("//a[text()='Cancel']")
Cancel_btn.click()

User_name_text=driver.find_element_by_xpath("//div[@id='usernamegroup']/label")
print(User_name_text.text)


