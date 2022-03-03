from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class Toolbar:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
    def home_page(self):
        return self.driver.find_element(By.ID,"Layer_1")
    def serach_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[data-ng-click='openSearchProducts()']")

    def user_icon(self):
        return self.driver.find_element(By.ID,"menuUser")
    def cart_icon(self):
        return self.driver.find_element(By.ID,"shoppingCartLink")
    def help_icon(self):
        return self.driver.find_element(By.ID,"helpLink")
    def go_home(self):
        self.home_page().click()
    def search_text(self,text:str):
        self.serach_icon().click()
        textbox=self.driver.find_element(By.ID,"autoComplete")
        textbox.send_keys(text)
        click=self.serach_icon()
        click.click()
    def open_cart_page(self):
        self.cart_icon().click()
    def hover_cart(self):
        hover=ActionChains(self.driver).move_to_element(self.cart_icon())
        hover.perform()
    def total_quantity_text(self):
        return self.driver.find_element(By.CSS_SELECTOR,"span>label.roboto-regular").text


    



