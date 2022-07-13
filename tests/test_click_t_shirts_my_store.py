import time

import pytest

from PageObject.click_t_shirts_my_store import clichome


@pytest.mark.usefixture("browser")
def test_click_t_shirts_my_store(browser):
    my_store_page = clichome(browser)
    my_store_page.go_to_site()
    time.sleep(5)
    my_store_page.click_T_SHIRTS()
    time.sleep(5)
    my_store_page.name_stranici()
    time.sleep(5)
    assert my_store_page.name_stranici() == "T-shirts"
