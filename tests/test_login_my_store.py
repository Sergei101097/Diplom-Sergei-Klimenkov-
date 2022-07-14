import time

import pytest

from PageObject.login_my_store import Clichome


@pytest.mark.usefixture("browser")
def test_login_to_the_authentication_page(browser):
    authentication = Clichome(browser)
    authentication.go_to_site()
    time.sleep(5)
    authentication.click_enter()
    time.sleep(5)
    authentication.authentication()
    assert authentication.authentication() == "AUTHENTICATION"


# Invalid email address
@pytest.mark.usefixture("browser")
def test_enter_my_store_Invalid_email_address(browser):
    my_store_page = Clichome(browser)
    my_store_page.go_to_site()
    time.sleep(5)
    my_store_page.click_enter()
    time.sleep(5)
    my_store_page.click_create_an_account()
    time.sleep(10)
    re = my_store_page.Invalid_email_address()
    time.sleep(10)
    assert re == "Invalid email address."


# YOUR PERSONAL INFORMATION
@pytest.mark.usefixture("browser")
def test_enter_my_store(browser):
    enter_my_store = Clichome(browser)
    enter_my_store.go_to_site()
    time.sleep(5)
    enter_my_store.click_enter()
    time.sleep(5)
    enter_my_store.click_email_address()
    time.sleep(5)
    enter_my_store.click_create_an_account()
    time.sleep(5)
    enter_my_store.your_personal_information()
    time.sleep(5)
    assert enter_my_store.your_personal_information() == "YOUR PERSONAL INFORMATION"


# YOUR PERSONAL INFORMATION
@pytest.mark.usefixture("browser")
def test_your_personal_information(browser):
    your_personal_information = Clichome(browser)
    your_personal_information.go_to_site()
    time.sleep(1)
    your_personal_information.click_enter()
    time.sleep(1)
    your_personal_information.click_email_address()
    time.sleep(5)
    your_personal_information.click_create_an_account()
    time.sleep(5)
    your_personal_information.Title()
    time.sleep(5)
    your_personal_information.First_name()
    time.sleep(1)
    your_personal_information.Last_name()
    time.sleep(1)
    your_personal_information.Email()
    time.sleep(1)
    your_personal_information.password()
    time.sleep(1)
    your_personal_information.date()
    time.sleep(1)
    your_personal_information.month()
    time.sleep(1)
    your_personal_information.year()
    time.sleep(1)
    your_personal_information.our_news()
    time.sleep(2)
    # YOUR ADDRESS
    your_personal_information.First_name_1()
    time.sleep(1)
    your_personal_information.Last_name_1()
    time.sleep(1)
    your_personal_information.Company("ОАО Минский автомобильный завод")
    time.sleep(1)
    your_personal_information.Address("Malonui 35")
    time.sleep(5)
    your_personal_information.Address_1("office 45,floor 8")
    time.sleep(5)
    your_personal_information.City()
    time.sleep(1)
    your_personal_information.State("Florida")
    time.sleep(1)
    your_personal_information.Zip_Postal_Code()
    time.sleep(1)
    your_personal_information.Country("United States")
    time.sleep(1)
    your_personal_information.Additional_information("fmgktrnohtrehnrehmjrtngiortnjhmfdsignekr")
    time.sleep(1)
    your_personal_information.Home_phone()
    time.sleep(1)
    your_personal_information.Mobile_phone()
    time.sleep(1)
    your_personal_information.Assign_an_address_alias_for_future_reference("Conter-wer")
    time.sleep(1)
    your_personal_information.click_register()
    time.sleep(15)
