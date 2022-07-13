import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
    yield driver
    driver.quit()


# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome((ChromeDriverManager().install()))
#     yield driver
#     driver.quit()
