import time

import pytest

from PageObject.ALREADY_REGISTERED import Clichome


@pytest.mark.usefixture("browser")
def test_ALREADY_REGISTERED(browser):
    ALREADY_REGISTERED = Clichome(browser)
    ALREADY_REGISTERED.go_to_site()
    time.sleep(2)
    ALREADY_REGISTERED.click_enter()
    time.sleep(2)
    ALREADY_REGISTERED.Email_address("klimenkovser@gmail.com")
    time.sleep(2)
    ALREADY_REGISTERED.Password("123456")
    time.sleep(2)
    ALREADY_REGISTERED.Sign_in()
    time.sleep(5)
    ALREADY_REGISTERED.ACCOUNT()
    assert ALREADY_REGISTERED.ACCOUNT() == "MY ACCOUNT"
