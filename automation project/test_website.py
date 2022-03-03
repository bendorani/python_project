from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Main_page import Main_page
from Toolbar import Toolbar
from Cart_page import Cart_page
from Category_page import Category_page
from Product_page import Product_page
from Helptest import Helptest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from Account_page import Account_page

class TestWebsite(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.main_page=Main_page(self.driver)
        self.toolbar=Toolbar(self.driver)
        self.cart_page=Cart_page(self.driver)
        self.category_page=Category_page(self.driver)
        self.product_page=Product_page(self.driver)
        self.help_Test=Helptest(self.driver)
        self.account_page=Account_page(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_number1(self):
        self.help_Test.order_num_products(2)
        sleep(2)
        sum1=0
        for i in self.help_Test.list_quantity1:
            sum1+=i

        self.assertEqual("("+str(sum1)+" Items)",self.cart_page.total_quantity_number_window().text)

    def test_number2(self):
        self.help_Test.order_num_products(3)
        for i in range(3):
            print(self.help_Test.list_price1)
            print(self.help_Test.list_name1)
            print(self.help_Test.list_quantity1)
            print(self.help_Test.list_color1)
            self.assertEqual(self.cart_page.cart_window_productscolor()[i].text, self.help_Test.list_color()[len(self.help_Test.list_price()) - 1 - i])
            self.assertEqual(self.cart_page.cart_window_productquantity()[i].text, 'QTY: ' + str(self.help_Test.list_quantity()[len(self.help_Test.list_quantity()) - 1 - i]))
            self.assertEqual(self.cart_page.cart_window_productprice()[i].text.replace(',', ''), '$' + str(self.help_Test.list_quantity()[len(self.help_Test.list_quantity()) - 1 - i] * self.help_Test.list_quantity()[len(self.help_Test.list_quantity()) - 1 - i]))


    def test_number3(self):
        self.help_Test.order_num_products(2)
        self.cart_page.remove_product()
        self.assertEqual(len(self.cart_page.cart_window_productnames()),1)

    def test_number4(self):
        self.help_Test.order_num_products(2)
        self.toolbar.open_cart_page()
        wait=WebDriverWait(self.driver,10)
        wait.until(Ec.text_to_be_present_in_element((By.CSS_SELECTOR,"a.select"),"SHOPPING CART"))
        self.assertEqual(self.cart_page.Shopping_cart_name().text,"SHOPPING CART")

    def test_number5(self):
        self.help_Test.order_num_products(3)
        list1=self.cart_page.cart_window_productquantity()
        list2=self.cart_page.cart_window_productprice()
        self.toolbar.open_cart_page()
        self.cart_page.Shoping_cart_table()
        self.assertEqual(self.cart_page.quantity_in_table(),list1)
        self.assertEqual(self.cart_page.price_in_table(),list2)
        self.assertEqual(self.cart_page.cart_total_in_window(),self.cart_page.cart_total_table())

    def test_number6(self):
        self.main_page.open_tablets()
        self.category_page.open_product_1()
        self.product_page.add_quantity()
        self.product_page.add_to_cart()
        self.toolbar.go_home()
        self.main_page.open_speakers()
        self.category_page.open_product2()
        self.product_page.add_to_cart()
        self.toolbar.open_cart_page()
        list1=self.cart_page.quantity_in_table()
        self.toolbar.go_home()
        self.main_page.open_laptops()
        self.category_page.open_product_1()
        self.product_page.add_quantity()
        self.product_page.add_to_cart()
        self.toolbar.go_home()
        self.main_page.open_speakers()
        self.category_page.open_product2()
        self.product_page.add_to_cart()
        self.toolbar.open_cart_page()
        self.assertNotEqual(list1,self.cart_page.quantity_in_table())
        self.assertEqual(self.cart_page.quantity_in_table(),['2','4'])

    def test_number7(self):
        self.main_page.open_tablets()
        self.category_page.open_product_1()
        self.driver.back()
        self.assertEqual(self.category_page.name_of_category(),"TABLETS")
        self.driver.back()
        self.assertTrue(Ec.presence_of_element_located((By.CSS_SELECTOR,".categoryCell")))

    def test_number8(self):
        self.help_Test.order_num_products(2)
        self.cart_page.Checkout()
        self.account_page.crateuser("Bend222","Ben12@gmail.com","Ben1234")
        self.account_page.safepay_pay("Aviel122","Avi123")
        self.assertTrue(self.account_page.order_succseed()==True)
        self.toolbar.hover_cart()
        self.assertTrue(self.cart_page.empty_cart_window()==True)
        self.account_page.my_orders()
        self.assertEqual(len(self.account_page.table_orders())-1,len(self.help_Test.list_quantity1))
        self.account_page.delete_account()






















