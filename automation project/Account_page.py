from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from Toolbar import Toolbar

class Account_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.toolbar=Toolbar(self.driver)
    def registration_button(self):
        self.driver.find_element(By.ID,"registration_btnundefined").click()

    def username(self,username:str):
        self.driver.find_element(By.NAME,"usernameRegisterPage").send_keys(username)
    def email(self,email:str):
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(email)
    def password(self,password:str):
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(password)
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(password)
    def register(self):
        self.driver.find_element(By.NAME,"i_agree").click()
        self.driver.find_element(By.ID,"register_btnundefined").click()
    def next_order_payment(self):
        self.driver.find_element(By.ID,"next_btn").click()
    def safepay_method(self):
        self.driver.find_element(By.NAME,"safepay").click()
    def safepay_username(self,username:str):
        self.driver.find_element(By.NAME,"safepay_username").send_keys(username)
    def safepay_password(self,password:str):
        self.driver.find_element(By.NAME,"safepay_password").send_keys(password)
    def Paynow(self):
        self.driver.find_element(By.ID,"pay_now_btn_SAFEPAY").click()

    def safepay_pay(self,username,password):
        self.next_order_payment()
        self.safepay_method()
        self.safepay_username(username)
        self.safepay_password(password)
        self.Paynow()
    def crateuser(self,username,email,password):
        self.registration_button()
        self.username(username)
        self.email(email)
        self.password(password)
        self.register()
    def my_orders(self):
        wait=WebDriverWait(self.driver,20)
        wait.until(Ec.element_to_be_clickable((By.ID,"menuUser")))
        self.toolbar.user_icon().click()
        wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,"[translate='MY_ORDERS']")))
        self.driver.find_element(By.CSS_SELECTOR,"[translate='MY_ORDERS']").click()
    def table_orders(self):
        table = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")
        return table

    def order_succseed(self):
        wait=WebDriverWait(self.driver,10)
        if wait.until(Ec.presence_of_element_located((By.ID,"orderPaymentSuccess"))):
            return True
        return False
    def delete_account(self):
        wait= WebDriverWait(self.driver,10)
        self.toolbar.user_icon().click()
        self.driver.find_element(By.CSS_SELECTOR,"a>div>label[translate='My_account']").click()
        self.driver.find_element(By.CSS_SELECTOR,"button.deleteMainBtnContainer").click()
        wait.until(Ec.visibility_of_element_located((self.driver.find_element(By.ID,"deleteAccountPopup"))))
        self.driver.find_element(By.NAME,"deleteRed").click()



