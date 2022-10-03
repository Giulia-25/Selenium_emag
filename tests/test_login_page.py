from time import sleep

import pytest
from assertpy import soft_assertions, assert_that

from pages.login_page import LoginPage
from pages.multi_factor_auth import MultiFactorAuth

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


def test_check_login_page(browser, login_page):
    login_page.load_page()
    with soft_assertions():
        assert_that(login_page.get_title_page()).is_equal_to("Salut!")
        assert_that(browser.current_url).is_equal_to(login_page.URL)
        assert_that(login_page.is_submit_button_displayed()).is_true()


def test_check_login_successfully(browser, login_page):
    login_page.load_page()
    login_page.insert_email("lzr.giulia@gmail.com")
    login_page.click_submit_button()
    sleep(5)
    login_page.insert_password("Blabla$25")
    login_page.click_submit_button()
    multi_factor_auth = MultiFactorAuth(browser)
    assert_that(browser.current_url).is_equal_to(multi_factor_auth.URL)
    assert_that(multi_factor_auth.is_activate_later_button_displayed()).is_true()
    multi_factor_auth.click_activate_later_button()
