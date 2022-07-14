import time

import pytest

from PageObject.product_in_the_cart import Clichome


@pytest.mark.usefixture("browser")
def test_product_in_the_cart(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.women_tab()
    time.sleep(2)
    my_store_page.select_dress()
    time.sleep(2)
    my_store_page.add_to_cart()
    time.sleep(2)
    my_store_page.dress_in_cart()
    time.sleep(2)
    assert my_store_page.dress_in_cart() == "Product successfully added to your shopping cart"
