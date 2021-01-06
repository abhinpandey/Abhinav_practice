import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(9)

Search_btn=driver.find_element_by_xpath("//input[@type='search']")
Search_btn.send_keys("ber")

count=driver.find_elements_by_xpath("//div[@class='product']")

counts=len(count)
assert counts== 3
time.sleep(4)
Add_to_cart=driver.find_elements_by_xpath("//div[@class='product-action']/button")

for btn in Add_to_cart:
    time.sleep(10)
    btn.click()
cart=driver.find_element_by_xpath("//a[@class='cart-icon']/img")
cart.click()

proceed_to_checkout=driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
proceed_to_checkout.click()

promo_Code_TextBox=driver.find_element_by_xpath("//input[@class='promoCode']")

Explicit_wait=WebDriverWait(driver,8)
time.sleep(4)
# Explicit_wait.until(expected_conditions.presence_of_element_located(promo_Code_TextBox))


promo_Code_TextBox.send_keys("rahulshettyacademy")

Apply_btn=driver.find_element_by_class_name("promoBtn")
Apply_btn.click()
# Explicit_wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@class='promoCode']")))

promo_inf0=driver.find_element_by_class_name("promoInfo")
print(promo_inf0.text)


