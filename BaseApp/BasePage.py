from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://automationpractice.com/"

    def find_element(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}"
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def api(self):
        return requests.get(self.base_url)
