import pytest

from PageObject.click_BEST_SELLERS_POPULAR import Clichome


@pytest.mark.usefixture("browser")
def test_get_locations_for_us_90210_check_status_code_equals_200():
    my_store_page = Clichome("browser")
    res = my_store_page.api()
    assert res.status_code == 200
