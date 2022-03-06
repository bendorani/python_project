from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from random import choice
from Toolbar import Toolbar
from Product_page import Product_page
class Main_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.toolbar=Toolbar(self.driver)
        self.product_page=Product_page(self.driver)

    def speakers_element(self):
        return self.driver.find_element(By.ID,"speakersImg")
    def mice_element(self):
        return self.driver.find_element(By.ID,"miceImg")
    def tablets_element(self):
        return self.driver.find_element(By.ID,"tabletsImg")
    def headphones_element(self):
        return self.driver.find_element(By.ID,"headphonesImg")
    def laptops_element(self):
        return self.driver.find_element(By.ID,"laptopsImg")
    def open_rand_category_page(self):
        list_categories=self.driver.find_elements(By.CSS_SELECTOR,".categoryCell")
        category_page=choice(list_categories)
        category_page.click()
    def open_laptops(self):
        self.laptops_element().click()
    def open_mice(self):
        self.mice_element().click()
    def open_tablets(self):
        self.tablets_element().click()
    def open_headphones(self):
        self.headphones_element().click()
    def open_speakers(self):
        self.speakers_element().click()
    def name_mainpage(self):
        if Ec.presence_of_element_located((By.CSS_SELECTOR,".categoryCell")):
            return True
        return False

    def login_from_icon(self,username,password):

        while True:
            try:
                self.toolbar.user_icon().click()
                self.driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(username)
                self.driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)
                self.driver.find_element(By.ID,"sign_in_btnundefined").click()
                break
            except:
                pass

    def log_out(self):
        while True:
            try:
                self.driver.find_element(By.ID,"menuUser").click()
                break
            except:
                pass
        self.driver.find_element(By.CSS_SELECTOR,"[ng-click='signOut($event)']").click()


    def login_check_element(self):
        if self.driver.find_element(By.CSS_SELECTOR,"#menuUserLink>span").text!="":
            return True
        return False
    def create_user_button(self):
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, "[data-ng-click='createNewAccount()']").click()
                break
            except:
                pass
        if self.driver.find_element(By.CSS_SELECTOR,".invalid"):
            self.driver.find_element(By.CSS_SELECTOR, "[data-ng-click='createNewAccount()']").click()
















