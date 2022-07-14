import time

import pytest

from PageObject.my_addresses import Clichome


@pytest.mark.usefixture("browser")
def test_my_addresses(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.email_address("klimenkovser@gmail.com")
    my_store_page.password("123456")
    time.sleep(2)
    my_store_page.sign_in()
    time.sleep(2)
    my_store_page.my_addresses()
    time.sleep(5)
    my_store_page.my_addresses_txt()
    time.sleep(5)
    assert my_store_page.my_addresses_txt() == "MY ADDRESSES"
