from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import choice
class Main_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

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







