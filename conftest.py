import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# @pytest.fixture
# def user_update(browser):
#     yield browser
#
#     browser.find_element()
