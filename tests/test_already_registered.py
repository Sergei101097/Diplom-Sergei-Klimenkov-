import time

import pytest

from PageObject.already_registered import Clichome


@pytest.mark.usefixture("browser")
def test_ALREADY_REGISTERED(browser):
    ALREADY_REGISTERED = Clichome(browser)
    ALREADY_REGISTERED.go_to_site()
    time.sleep(2)
    ALREADY_REGISTERED.click_enter()
    time.sleep(2)
    ALREADY_REGISTERED.email_address("klimenkovser@gmail.com")
    time.sleep(2)
    ALREADY_REGISTERED.password("123456")
    time.sleep(2)
    ALREADY_REGISTERED.sign_in()
    time.sleep(5)
    ALREADY_REGISTERED.account()
    assert ALREADY_REGISTERED.account() == "MY ACCOUNT"
