from selenium.webdriver.common.by import By

from BaseApp.BasePage import BasePage

class MyStoreClickLocators:
    LOCATOR_MY_STORE_CLICK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")
    LOCATOR_MY_STORE_SELECTOR = (By.CLASS_NAME, "category-name")


class Clichome(BasePage):
    def click_dresses(self):
        return self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_CLICK, time=50).click()

    def name_stranici(self):
        selector_women = self.find_element(MyStoreClickLocators.LOCATOR_MY_STORE_SELECTOR, time=50).text
        return selector_women
