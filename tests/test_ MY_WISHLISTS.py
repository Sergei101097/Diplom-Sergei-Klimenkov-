import time

import pytest

from PageObject.MY_WISHLISTS import clichome


@pytest.mark.usefixture("browser")
def test_my_wishlists(browser):
    my_store_page = clichome(browser)
    time.sleep(2)
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
    my_store_page.MY_WISHLISTS()
    time.sleep(2)
    my_store_page.MY_WISHLISTS_TXT()
    time.sleep(2)
    assert my_store_page.MY_WISHLISTS_TXT() == "MY WISHLISTS"
