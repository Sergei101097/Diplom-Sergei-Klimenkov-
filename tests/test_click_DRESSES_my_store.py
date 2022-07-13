import pytest

from PageObject.click_DRESSES_my_store import clichome


@pytest.mark.usefixture("browser")
def test_click_DRESSES_my_store(browser):
    my_store_page = clichome(browser)
    my_store_page.go_to_site()
    my_store_page.click_DRESSES()
    my_store_page.name_stranici()
    assert my_store_page.name_stranici() == "Dresses"
