import time

import pytest

from PageObject.cart_empty import Clichome


@pytest.mark.usefixture("browser")
def test_my_addresses(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.email_address("klimenkovser@gmail.com")
    time.sleep(2)
    my_store_page.password("123456")
    time.sleep(2)
    my_store_page.sign_in()
    time.sleep(2)
    my_store_page.cart()
    time.sleep(2)
    my_store_page.cart_empty()
    time.sleep(2)
    assert my_store_page.cart_empty() == "Your shopping cart is empty."
