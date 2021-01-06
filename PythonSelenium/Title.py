from selenium import webdriver

# driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver=webdriver.Firefox(executable_path="E:\\Selenium\\Drivers\\geckodriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/#/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()