import time

import pytest

from PageObject.click_BEST_SELLERS_POPULAR import clichome


@pytest.mark.usefixture("browser")
def test_click_BEST_SELLERS_POPULAR(browser):
    my_store_page = clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_POPULAR()
    time.sleep(2)
    my_store_page.click_BEST_SELLERS()
    time.sleep(2)
