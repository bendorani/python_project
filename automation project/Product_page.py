from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Product_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
    def minus_quantity_element(self):
      return self.driver.find_element(By.CLASS_NAME,"minus")
    def plus_quantity_element(self):
        return self.driver.find_element(By.CLASS_NAME,"plus")
    def number_quantity_element(self):
        return self.driver.find_element(By.NAME,"quantity")

    def add_quantity(self):
        self.plus_quantity_element().click()
    def remove_quantity(self):
        self.minus_quantity_element().click()
    def set_quantity(self,num:int):
        self.number_quantity_element().send_keys(num)
    def add_to_cart_element(self):
        return self.driver.find_element(By.NAME,"save_to_cart")
    def price_element(self):
        price=self.driver.find_elements(By.CSS_SELECTOR,"h2.screen768")
        return price[0]
    def color_element(self):
        color=self.driver.find_element(By.CSS_SELECTOR,".colorSelected")
        return color
    def name_element(self):
        return self.driver.find_element(By.CSS_SELECTOR,"h1.screen768")
    def add_to_cart(self):
        self.add_to_cart_element().click()










