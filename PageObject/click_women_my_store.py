from selenium.webdriver.common.by import By

from BaseApp.BasePage import BasePage


class MyStoreClickLocators:
    LOCATOR_MY_STORE_CLICK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    LOCATOR_MY_STORE_CLASS_NAME = (By.CLASS_NAME, "category-name")


class Clichome(BasePage):
    def click_women(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK, time=10).click()

    def name_stranici(self):
        selector_women = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLASS_NAME, time=10).text
        return selector_women
