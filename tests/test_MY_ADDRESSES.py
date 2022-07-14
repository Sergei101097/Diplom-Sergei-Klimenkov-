import time

import pytest

from PageObject.MY_ADDRESSES import Clichome


@pytest.mark.usefixture("browser")
def test_my_addresses(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.Email_address("klimenkovser@gmail.com")
    my_store_page.Password("123456")
    time.sleep(2)
    my_store_page.Sign_in()
    time.sleep(2)
    my_store_page.MY_ADDRESSES()
    time.sleep(5)
    my_store_page.MY_ADDRESSES_TXT()
    time.sleep(5)
    assert my_store_page.MY_ADDRESSES_TXT() == "MY ADDRESSES"
