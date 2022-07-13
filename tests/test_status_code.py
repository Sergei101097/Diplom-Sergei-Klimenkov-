import pytest

from PageObject.click_BEST_SELLERS_POPULAR import clichome


@pytest.mark.usefixture("browser")
def test_get_locations_for_us_90210_check_status_code_equals_200():
    my_store_page = clichome("browser")
    res = my_store_page.api()
    assert res.status_code == 200
