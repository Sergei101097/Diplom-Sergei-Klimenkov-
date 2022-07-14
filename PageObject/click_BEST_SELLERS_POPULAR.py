from selenium.webdriver.common.by import By

from BaseApp.BasePage import BasePage


class MyStoreClickLocators:
    LOCATOR_BEST_SELLERS_MY_STORE_CLICK = (By.XPATH, "//*[@id='home-page-tabs']/li[2]/a")
    LOCATOR_POPULAR_MY_STORE_CLICK = (By.XPATH, "//*[@id='home-page-tabs']/li[1]/a")


class Clichome(BasePage):
    def click_POPULAR(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_POPULAR_MY_STORE_CLICK, time=50).click()

    def click_BEST_SELLERS(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_BEST_SELLERS_MY_STORE_CLICK, time=50).click()
