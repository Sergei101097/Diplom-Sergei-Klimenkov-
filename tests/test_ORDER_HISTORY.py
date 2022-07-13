import time

import pytest

from PageObject.my_accaunt import clichome


@pytest.mark.usefixture("browser")
def test_my_accaunt(browser):
    my_store_page = clichome(browser)
    time.sleep(5)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.Email_address("klimenkovser@gmail.com")
    my_store_page.Password("123456")
    time.sleep(2)
    my_store_page.Sign_in()
    time.sleep(2)
    my_store_page.HISTORY_AND_DETAILS()
    time.sleep(5)
    my_store_page.ORDER_HISTORY()
    time.sleep(10)
    assert my_store_page.ORDER_HISTORY() == "ORDER HISTORY"
