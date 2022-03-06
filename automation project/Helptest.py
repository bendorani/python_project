from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Toolbar import Toolbar
from Product_page import Product_page
from Main_page import Main_page
from Category_page import Category_page

class Helptest:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.main_page = Main_page(self.driver)
        self.product_page = Product_page(self.driver)
        self.toolbar = Toolbar(self.driver)
        self.category_page = Category_page(self.driver)
        self.list_color1=[]
        self.list_name1=[]
        self.list_price1=[]
        self.list_quantity1=[]

    def order_num_products(self,num:int):
        for i in range(num):
            self.main_page.open_rand_category_page()
            self.category_page.open_productpage()
            for j in range(i+1):
                self.product_page.add_quantity()
            self.list_price1.append(float(self.product_page.price_element().text.replace(',', '').replace('$', '')))
            self.list_name1.append(self.product_page.name_element().text)
            self.list_color1.append(self.product_page.color_element().get_attribute("title"))
            self.list_quantity1.append(int(self.product_page.number_quantity_element().get_attribute("value")))
            self.product_page.add_to_cart()
            self.toolbar.go_home()
        self.toolbar.hover_cart()

    def list_price(self):
        return self.list_price1[::-1]
    def list_quantity(self):
        return self.list_quantity1[::-1]
    def list_name(self):
        return self.list_name1[::-1]
    def list_color(self):
        return self.list_color1[::-1]
