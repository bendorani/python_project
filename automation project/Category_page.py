from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import choice
from Main_page import Main_page

class Category_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.list_elemnts=[]
    def product_elemnts(self):
        products_in_stock=self.driver.find_elements(By.CLASS_NAME,"imgProduct")
        return products_in_stock
    def open_productpage(self):
        element=choice(self.product_elemnts())
        while element.get_attribute("class")=="imgProduct outOfStock" or element in self.list_elemnts :
            element = choice(self.product_elemnts())
        else:
            self.list_elemnts.append(element)
            element.click()

    def open_product_1(self):
        self.driver.find_element(By.ID,'16').click()

    def open_product2(self):
        self.driver.find_element(By.ID,'20').click()

    def name_of_category(self):
        return self.driver.find_element(By.CSS_SELECTOR,'.categoryTitle').text




