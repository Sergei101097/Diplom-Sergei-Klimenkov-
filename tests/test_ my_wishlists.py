import time

import pytest

from PageObject.my_wishlists import Clichome


@pytest.mark.usefixture("browser")
def test_my_wishlists(browser):
    my_store_page = Clichome(browser)
    time.sleep(2)
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
    my_store_page.my_wishlists()
    time.sleep(2)
    my_store_page.my_wishlists_txt()
    time.sleep(2)
    assert my_store_page.my_wishlists_txt() == "MY WISHLISTS"
