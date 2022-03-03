from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import choice
from Main_page import Main_page

class Category_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
    def product_elemnts(self):
        products_in_stock=self.driver.find_elements(By.CLASS_NAME,"imgProduct")
        products_out=self.driver.find_elements(By.CLASS_NAME,"outOfStock")
        for i in products_in_stock:
            if i in products_out:
                products_in_stock.remove(i)
        return products_in_stock
    def open_productpage(self):
        element=choice(self.product_elemnts())
        element.click()
    def open_product_1(self):
        self.driver.find_element(By.ID,'16').click()

    def open_product2(self):
        self.driver.find_element(By.ID,'20').click()

    def name_of_category(self):
        return self.driver.find_element(By.CSS_SELECTOR,'.categoryTitle').text




