import time

import pytest

from PageObject.Cart_empty import Clichome


@pytest.mark.usefixture("browser")
def test_my_addresses(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.Email_address("klimenkovser@gmail.com")
    time.sleep(2)
    my_store_page.Password("123456")
    time.sleep(2)
    my_store_page.Sign_in()
    time.sleep(2)
    my_store_page.CART()
    time.sleep(2)
    my_store_page.CART_EMPTY()
    time.sleep(2)
    assert my_store_page.CART_EMPTY() == "Your shopping cart is empty."
