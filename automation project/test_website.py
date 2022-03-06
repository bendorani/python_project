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
        self.driver.get("http://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)
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

        sum1=0
        for i in self.help_Test.list_quantity1:
            sum1+=i

        self.assertEqual("("+str(sum1)+" Items)",self.cart_page.total_quantity_number_window().text)

    def test_number2(self):
        self.help_Test.order_num_products(3)
        print(self.help_Test.list_price1)
        print(self.help_Test.list_name1)
        print(self.help_Test.list_quantity1)
        print(self.help_Test.list_color1)
        for i in range(3):
            self.assertEqual(self.cart_page.cart_window_productscolor()[i].text, self.help_Test.list_color()[i])
            self.assertEqual(self.cart_page.cart_window_productquantity()[i], str(self.help_Test.list_quantity()[i]))
            self.assertEqual(float(self.cart_page.cart_window_productprice()[i]) ,float(self.help_Test.list_price()[i] * self.help_Test.list_quantity()[i]))
            # self.assertEqual(self.cart_page.cart_window_productnames()[i].text,self.help_Test.list_name()[i])


    def test_number3(self):
        self.help_Test.order_num_products(2)
        self.cart_page.remove_product()
        self.cart_page.cart_window_productnames()
        self.assertEqual(len(self.cart_page.cart_window_productnames()),1)
        self.assertNotIn(self.help_Test.list_name(),self.cart_page.cart_window_productnames())

    def test_number4(self):
        self.help_Test.order_num_products(2)
        self.toolbar.open_cart_page()
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
        self.help_Test.order_num_products(2)
        self.toolbar.open_cart_page()
        self.cart_page.edit_products()
        print(self.help_Test.list_quantity1)
        self.assertNotEqual(self.cart_page.quantity_in_table(),self.help_Test.list_quantity1)
        self.assertEqual(self.cart_page.quantity_in_table(),['3','4'])

    def test_number7(self):
        self.main_page.open_tablets()
        self.category_page.open_product_1()
        self.driver.back()
        self.assertEqual(self.category_page.name_of_category(),"TABLETS")
        self.driver.back()
        sleep(2)
        self.assertTrue(self.main_page.name_mainpage()==True)

    def test_number8(self):
        self.help_Test.order_num_products(2)
        self.cart_page.Checkout()
        self.account_page.registration_button()
        self.account_page.createuser("Bend20987","Ben12@gmail.com","Ben123")
        self.account_page.next_order_payment()
        self.account_page.safepay_pay("Aviel122","Avi123")
        self.assertTrue(self.account_page.order_succseed()==True)
        self.toolbar.hover_cart()
        self.assertTrue(self.cart_page.empty_cart_window()==True)
        self.toolbar.go_home()
        self.account_page.my_orders()
        self.assertEqual(self.account_page.table_orders(),len(self.help_Test.list_quantity1))
        self.assertEqual(self.account_page.name_of_products_in_order(),self.help_Test.list_name())
    def test_number9(self):
        self.help_Test.order_num_products(2)
        self.cart_page.Checkout()
        self.account_page.login_after_checkout("Bend20987","Ben123")
        self.account_page.credit_card_pay(123456789123,234,"Bend","03","2027")
        self.assertTrue(self.account_page.order_succseed()==True)
        self.toolbar.hover_cart()
        self.assertTrue(self.cart_page.empty_cart_window()==True)
        self.toolbar.go_home()
        self.account_page.my_orders()
        print(self.account_page.table_orders())
        print(self.help_Test.list_quantity1)
        self.assertEqual(self.account_page.table_orders(),len(self.help_Test.list_quantity1))
    def test_number10(self):
        self.toolbar.user_icon().click()
        self.main_page.create_user_button()
        self.account_page.createuser("Bend2018","Bendo101@gmail.com","Ben12367")
        self.toolbar.go_home()
        sleep(2)
        self.main_page.log_out()
        sleep(2)
        self.assertTrue(self.main_page.login_check_element()==False)
        self.main_page.login_from_icon("Bend2018","Ben12367")
        sleep(2)
        self.assertTrue(self.main_page.login_check_element() ==True)



























