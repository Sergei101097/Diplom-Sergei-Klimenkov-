import time

import pytest

from PageObject.click_best_sellers_popular import Clichome


@pytest.mark.usefixture("browser")
def test_click_BEST_SELLERS_POPULAR(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_popular()
    time.sleep(2)
    my_store_page.click_best_sellers()
    time.sleep(2)
