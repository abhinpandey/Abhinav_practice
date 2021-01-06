import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
Search_btn=driver.find_element_by_xpath("//input[@type='search']")
Search_btn.send_keys("ber")
time.sleep(4)
count=driver.find_elements_by_xpath("//div[@class='product']")
time.sleep(4)
counts=len(count)
assert counts== 3

Add_to_cart=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for btn in Add_to_cart:
    btn.click()
cart=driver.find_element_by_xpath("//a[@class='cart-icon']/img")
cart.click()

proceed_to_checkout=driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
proceed_to_checkout.click()

promo_Code_TextBox=driver.find_element_by_xpath("//input[@class='promoCode']")
promo_Code_TextBox.send_keys("rahulshettyacademy")

Apply_btn=driver.find_element_by_class_name("promoBtn")
Apply_btn.click()

promo_inf0=driver.find_element_by_class_name("promoInfo")
print(promo_inf0.text)


