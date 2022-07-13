from selenium.webdriver.common.by import By

from BaseApp.BasePage import BasePage


class MyStoreClickLocators:
    LOCATOR_WOMEN_TAB = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    LOCATOR_DRESS = (By.XPATH, "//*[@id='special_block_right']/div/ul/li/a/img")
    LOCATOR_ADD_CART_BUTTON = (By.NAME, "Submit")
    LOCATOR_DRESS_IN_CART = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[1]/h2")


class clichome(BasePage):
    def women_tab(self):
        search_women_tab = self.find_element(MyStoreClickLocators.LOCATOR_WOMEN_TAB, time=50)
        search_women_tab.click()
        return search_women_tab

    def select_dress(self):
        search_dress = self.find_element(MyStoreClickLocators.LOCATOR_DRESS, time=50)
        search_dress.click()
        return search_dress

    def add_to_cart(self):
        search_button_cart = self.find_element(MyStoreClickLocators.LOCATOR_ADD_CART_BUTTON, time=50)
        search_button_cart.click()
        return search_button_cart

    def dress_in_cart(self):
        se = self.find_element(MyStoreClickLocators.LOCATOR_DRESS_IN_CART, time=50).text
        return se
