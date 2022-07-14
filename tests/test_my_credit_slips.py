import time

import pytest

from PageObject.my_credit_slips import Clichome


@pytest.mark.usefixture("browser")
def test_my_credit(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(2)
    my_store_page.click_enter()
    time.sleep(2)
    my_store_page.email_address("klimenkovser@gmail.com")
    my_store_page.password("123456")
    time.sleep(2)
    my_store_page.sign_in()
    time.sleep(2)
    my_store_page.my_credit_slips()
    time.sleep(5)
    my_store_page.credit_slips()
    time.sleep(5)
    assert my_store_page.credit_slips() == "CREDIT SLIPS"
