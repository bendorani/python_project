from selenium import webdriver
from selenium.webdriver.common.by import By
from Product_page import Product_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class Cart_page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.product_page = Product_page(self.driver)


    def total_quantity_number_window(self):
        return self.driver.find_element(By.CSS_SELECTOR,"span>label.roboto-regular")

    def cart_window_productprice(self):
        list_prices=[]
        prices=self.driver.find_elements(By.CSS_SELECTOR,"p.price")
        for i in prices:
            list_prices.append(i.text.replace("$","").replace(",",""))
        return list_prices
    def cart_window_productnames(self):
        names=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>a>h3")
        return names

    def cart_window_productscolor(self):
        colors=self.driver.find_elements(By.CSS_SELECTOR,"label>span.ng-binding")
        return colors

    def cart_window_productquantity(self):
        quantitys=self.driver.find_elements(By.CSS_SELECTOR,"td>a>label.ng-binding")
        list_quantity=[]
        for i in range(0,len(quantitys),2):
            list_quantity.append(quantitys[i].text.replace('QTY: ',''))
        return list_quantity
    def remove_product(self):
        self.driver.find_element(By.CLASS_NAME,"removeProduct").click()

    def Shopping_cart_name(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(Ec.text_to_be_present_in_element((By.CSS_SELECTOR,"a.select"),"SHOPPING CART"))
        return self.driver.find_element(By.CSS_SELECTOR,"a.select")

    def Shoping_cart_table(self):
        list2=[]
        list_tr=self.driver.find_elements(By.CSS_SELECTOR,"#shoppingCart>table>tbody>tr")
        for i in list_tr:
            list_td=i.find_elements(By.TAG_NAME,"td")
            list2.append(list_td[1].text)
            list2.append(list_td[3].find_element(By.TAG_NAME,"span").get_attribute("title"))
            list2.append(list_td[4].text)
            list2.append(list_td[5].find_element(By.TAG_NAME,"p").text)
            print(list2)
            list2=[]
    def quantity_in_table(self):
        list2=[]
        list_tr = self.driver.find_elements(By.CSS_SELECTOR, "#shoppingCart>table>tbody>tr")
        for i in list_tr:
            list_td = i.find_elements(By.TAG_NAME, "td")
            list2.append(list_td[4].text)
        return list2

    def price_in_table(self):
        list3 = []
        list_tr = self.driver.find_elements(By.CSS_SELECTOR, "#shoppingCart>table>tbody>tr")
        for i in list_tr:
            list_td = i.find_elements(By.TAG_NAME, "td")
            list3.append(list_td[5].find_element(By.TAG_NAME,"p").text.replace("$","").replace(",",""))
        return list3
    def cart_total_in_window(self):
        total_window=self.driver.find_elements(By.CSS_SELECTOR,".cart-total")
        return total_window[0].text
    def cart_total_table(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"span.roboto-medium")[3].text
    def Checkout(self):
        self.driver.find_element(By.ID,"checkOutPopUp").click()

    def empty_cart_window(self):
        if self.driver.find_element(By.CSS_SELECTOR,"[translate='Your_shopping_cart_is_empty']"):
            return True
        return False

    def edit_quantity(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(Ec.invisibility_of_element_located((By.ID,"checkOutPopUp")))
        edit=self.driver.find_elements(By.LINK_TEXT,"EDIT")
        return edit
    def edit_products(self):
        for i in range(len(self.edit_quantity())-1):
            self.edit_quantity()[i].click()
            self.product_page.add_quantity()
            self.product_page.add_to_cart()












