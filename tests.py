import time

import pytest
from auth_rostelecom import SearchHelper
from auth_rostelecom import SearchLocator


def test_auth_valid_number(browser):
    "Позитивная проверка входа на страницу Ростелекома с валидными данными по номеру телефона"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.enter_username('89180782555')
    auth_page.enter_password('Bondareva12')
    auth_page.click_on_the_button_entry()
    assert auth_page.check_user_page(), 'Неверный логин или пароль'


def test_auth_invalid(browser):
    "Негативная проверка входа на страницу Ростелекома с невалидными данными"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.enter_username('83210000000')
    auth_page.enter_password('Booooo12')
    auth_page.click_on_the_button_entry()
    assert auth_page.check_error_auth_message()


def test_auth_valid_email(browser):
    "Позитивная проверка входа на страницу Ростелекома с валидными данными с использованием почты"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_email_entry()
    auth_page.enter_username('bondareva.nastya34@gmail.com')
    auth_page.enter_password('Bondareva12')
    auth_page.click_on_the_button_entry()
    assert auth_page.check_user_page(), 'Неверный логин или пароль'


def test_user_agreement_page(browser):
    "Проверка перехода на страницу Пользовательского соглашения"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_user_agreemenrs()
    for window_handle in browser.window_handles:
        if window_handle != browser.current_window_handle:
            browser.switch_to.window(window_handle)
            break
    assert browser.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


def test_help_page(browser):
    "Проверка перехода на страницу Помощь"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.open_help_page()
    element = SearchHelper.find_element(SearchLocator.LOCATOR_TEXT_HELP)
    assert element.is_displayed()
    # TODO Проверить почему тест упал. Предполагаю, что кнопка Помощь не была в поле зрения.Добавила изменения в методе
    #  open_help_page, тест так же падает. Проблема в проверке


@pytest.mark.parametrize("word", ['Alina', 'П', 'ПолинаИвановаСергеевна242628301'])
def test_validation_name(browser, word):
    "Проверка валидации поля 'Имя' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_firstname(word)
    auth_page.click_button_sing_up()
    # time.sleep(5)
    # element = SearchHelper.find_element(SearchLocator.LOCATOR_HINT_NAME)
    # assert element.is_displayed()
    # TODO Добавить проверку наличия текста с подсказкой о заполнении данного поля


@pytest.mark.parametrize("word", ['Pushkina', 'П', 'ПолинаИвановаСергеевна242628301'])
def test_validation_last_name(browser, word):
    "Проверка валидации поля 'Фамилия' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_lastname(word)
    auth_page.click_button_sing_up()
    # time.sleep(5)
    #TODO добавить проверку для данного теста


@pytest.mark.parametrize("word", ['12894638910', '@mail.com', '12ivanov@.ru', '+7918$579777', '9'])
def test_validation_email(browser, word):
    "Проверка валидации поля 'E-mail или мобильный телефон' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_email(word)
    auth_page.click_button_sing_up()
    #TODO добавить проверку для данного теста


def test_change_user_lastname(browser):
    "Проверить что при изменении Фамилии пользователя данные сохранятся"
    #TODO если буду добавлять данный тест, то может упасть проверка первого теста(авторизация с валидными данными)