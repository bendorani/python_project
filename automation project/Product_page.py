from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Product_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
    def minus_quantity(self):
      return self.driver.find_element(By.CLASS_NAME,"minus")
    def plus_quantity(self):
        return self.driver.find_element(By.CLASS_NAME,"plus")
    def number_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR,".ng-touched")
    def add_quantity(self):
        self.plus_quantity().click()
    def remove_quantity(self):
        self.minus_quantity().click()
    def set_quantity(self,num:int):
        self.number_quantity().send_keys(num)
    def add_to_cart_element(self):
        return self.driver.find_element(By.NAME,"save_to_cart")
    def add_to_cart(self):
        self.add_to_cart_element().click()
