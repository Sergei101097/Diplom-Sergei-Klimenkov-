from selenium.webdriver.common.by import By

from BaseApp.BasePage import BasePage


class MyStoreClickLocators:
    LOCATOR_MY_STORE_CLICK_ENTER = (By.CLASS_NAME, "login")
    LOCATOR_MY_STORE_CLICK_Email_address = (By.CSS_SELECTOR, "#email")
    LOCATOR_MY_STORE_CLICK_Password = (By.CSS_SELECTOR, "#passwd")
    LOCATOR_MY_STORE_CLICK_Sign_in = (By.CSS_SELECTOR, "#SubmitLogin")
    LOCATOR_MY_STORE_MY_CREDIT_SLIPS = (
        By.CSS_SELECTOR,
        "#center_column > div > div:nth-child(1) > ul > li:nth-child(2) > a",
    )
    LOCATOR_MY_STORE_CREDIT_SLIPS = (By.CSS_SELECTOR, "#center_column > h1")


class Clichome(BasePage):
    def click_enter(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_ENTER, time=20).click()

    def Email_address(self, wood):
        Email_address = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_Email_address, time=20)
        Email_address.send_keys(wood)

    def Password(self, wood):
        Password = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_Password, time=20)
        Password.send_keys(wood)

    def Sign_in(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK_Sign_in, time=20).click()

    def my_credit_slips(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_MY_CREDIT_SLIPS, time=20).click()

    def CREDIT_SLIPS(self):
        ORDER_HISTORY = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CREDIT_SLIPS, time=20).text
        return ORDER_HISTORY
