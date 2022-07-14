import pytest

from PageObject.click_dresses_my_store import Clichome


@pytest.mark.usefixture("browser")
def test_click_DRESSES_my_store(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    my_store_page.click_dresses()
    my_store_page.name_stranici()
    assert my_store_page.name_stranici() == "Dresses"
