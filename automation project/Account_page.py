from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from Toolbar import Toolbar
from selenium.webdriver.support.select import Select


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
        wait=WebDriverWait(self.driver,30)
        wait.until(Ec.presence_of_element_located((By.NAME,"i_agree")))
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
    def Pay_now_manual(self):
        self.driver.find_element(By.ID,"pay_now_btn_ManualPayment").click()

    def safepay_pay(self,username,password):
        self.next_order_payment()
        self.safepay_method()
        self.safepay_username(username)
        self.safepay_password(password)
        self.Paynow()
    def createuser(self,username,email,password):
        self.username(username)
        self.email(email)
        self.password(password)
        self.register()
    def my_orders(self):
        wait=WebDriverWait(self.driver,20)
        wait.until(Ec.presence_of_element_located((By.ID,"menuUser")))
        self.toolbar.user_icon().click()
        wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR,"a>div>label[translate='My_Orders']")))
        self.driver.find_element(By.CSS_SELECTOR,"a>div>label[translate='My_Orders']").click()
    def table_orders(self):
        table = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>img")
        return len(table)
    def name_of_products_in_order(self):
        list_names=[]
        names=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>span.ng-binding")
        for i in names:
            list_names.append(i.text.upper())
        return list_names

    def order_succseed(self):
        wait=WebDriverWait(self.driver,10)
        if wait.until(Ec.presence_of_element_located((By.ID,"orderPaymentSuccess"))):
            return True
        return False
    def delete_account(self):
        self.toolbar.user_icon().click()
        self.driver.find_element(By.CSS_SELECTOR,"button.deleteMainBtnContainer").click()
        self.driver.find_element(By.NAME,"deleteRed").click()

    def login_after_checkout(self, username: str, password: str):
        self.driver.find_element(By.NAME, 'usernameInOrderPayment').send_keys(username)
        self.driver.find_element(By.NAME, 'passwordInOrderPayment').send_keys(password)
        self.driver.find_element(By.ID, 'login_btnundefined').click()

    def credit_card_pay(self, number1, number2, name, dp_month, dp_year):
        self.next_order_payment()
        self.credit_card_method()
        self.card_number(number1)
        self.CVV_number(number2)
        self.cardholder_name_number(name)
        self.choose_month(dp_month)
        self.choose_year(dp_year)
        self.Pay_now_manual()

    def credit_card_method(self):
        self.driver.find_element(By.NAME, 'masterCredit').click()

    def card_number(self, number1: int):
        self.driver.find_element(By.NAME, 'card_number').send_keys(number1)

    def CVV_number(self, number2: int):
        self.driver.find_element(By.NAME, 'cvv_number').send_keys(number2)

    def cardholder_name_number(self, name: str):
        self.driver.find_element(By.NAME, 'cardholder_name').send_keys(name)

    def month_list(self):
       return self.driver.find_element(By.NAME, 'mmListbox')

    def choose_month(self, month):
        dp_month = Select(self.month_list())
        dp_month.select_by_visible_text(month)

    def year_list(self):
        return self.driver.find_element(By.NAME, 'yyyyListbox')

    def choose_year(self, year):
        dp_year = Select(self.year_list())
        dp_year.select_by_visible_text(year)






