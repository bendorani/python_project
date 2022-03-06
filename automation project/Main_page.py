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
        wait=WebDriverWait(self.driver,20)
        wait.until(Ec.visibility_of_element_located((By.ID,"menuUser")))
        self.toolbar.user_icon().click()
        wait.until(Ec.presence_of_element_located((By.NAME,"username")))
        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.ID,"sign_in_btnundefined").click()

    def log_out(self):
        wait=WebDriverWait(self.driver,20)
        wait.until(Ec.element_to_be_clickable((By.ID,"menuUser")))
        self.toolbar.user_icon().click()
        wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR,"[ng-click='signOut($event)']")))
        self.driver.find_element(By.CSS_SELECTOR,"[ng-click='signOut($event)']").click()

    def login_check_element(self):
        if self.driver.find_element(By.CSS_SELECTOR,"#menuUserLink>span").text!="":
            return True
        return False
    def create_user_button(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(Ec.element_to_be_clickable((By.LINK_TEXT,"CREATE NEW ACCOUNT")))
        self.driver.find_element(By.LINK_TEXT,"CREATE NEW ACCOUNT").click()
        if self.driver.find_element(By.CSS_SELECTOR,".invalid"):
            wait.until(Ec.element_to_be_clickable((By.LINK_TEXT, "CREATE NEW ACCOUNT")))
            self.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").click()












