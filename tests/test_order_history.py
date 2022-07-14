import time

import pytest

from PageObject.my_accaunt import Clichome


@pytest.mark.usefixture("browser")
def test_my_accaunt(browser):
    my_store_page = Clichome(browser)
    time.sleep(5)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.email_address("klimenkovser@gmail.com")
    my_store_page.password("123456")
    time.sleep(2)
    my_store_page.sign_in()
    time.sleep(2)
    my_store_page.histoty_and_details()
    time.sleep(5)
    my_store_page.order_history()
    time.sleep(10)
    assert my_store_page.order_history() == "ORDER HISTORY"
