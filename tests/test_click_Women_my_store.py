import time

import pytest

from PageObject.click_Women_my_store import Clichome


#@pytest.mark.usefixture("browser")
def test_click_Women_my_store(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(5)
    my_store_page.click_Women()
    time.sleep(5)
    my_store_page.name_stranici()
    time.sleep(5)
    assert my_store_page.name_stranici() == "Women"
