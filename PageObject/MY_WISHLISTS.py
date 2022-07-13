from selenium.webdriver.common.by import By

from BaseApp.BasePage import BasePage


class MyStoreClickLocators:
    LOCATOR_MY_STORE_CLICK_ENTER = (By.CLASS_NAME, "login")
    LOCATOR_MY_STORE_CLICK_Email_address = (By.CSS_SELECTOR, "#email")
    LOCATOR_MY_STORE_CLICK_Password = (By.CSS_SELECTOR, "#passwd")
    LOCATOR_MY_STORE_CLICK_Sign_in = (By.CSS_SELECTOR, "#SubmitLogin")
    LOCATOR_MY_STORE_MY_WISHLISTS = (
        By.CSS_SELECTOR,
        "#center_column > div > div:nth-child(2) > ul > li > a",
    )
    LOCATOR_MY_STORE_MY_WISHLISTS_TXT = (By.CSS_SELECTOR, "#mywishlist > h1")


class clichome(BasePage):
    def click_enter(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_ENTER, time=50).click()

    def Email_address(self, wood):
        Email_address = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_Email_address, time=50)
        Email_address.send_keys(wood)
        return Email_address

    def Password(self, wood):
        Password = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_Password, time=50)
        Password.send_keys(wood)
        return Password

    def Sign_in(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_Sign_in, time=50).click()

    def MY_WISHLISTS(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_MY_WISHLISTS, time=50).click()

    def MY_WISHLISTS_TXT(self):
        ORDER_HISTORY = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_MY_WISHLISTS_TXT, time=50).text
        return ORDER_HISTORY
