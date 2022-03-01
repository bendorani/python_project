from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import choice
from Main_page import Main_page

class Category_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
    def product_elemnts(self):
        products=self.driver.find_elements(By.CLASS_NAME,"imgProduct")
        return products
    def open_productpage(self):
        element=choice(self.product_elemnts())
        while element!=self.driver.find_element(By.CSS_SELECTOR,"[class='imgProduct outOfStock']"):
            element.click()
            break




