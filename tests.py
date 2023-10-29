import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def test_auth_valid_login(browser):
    "Позитивная проверка входа на страницу Ростелекома с валидными данными с использованием логина"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_login_entry()
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
    help_page = auth_page.linking_text_help()
    element = help_page.find_element(By.XPATH, "//h1[contains(text(),'Ваш безопасный ключ к сервисам')]")
    assert element.is_displayed()


# def test_auth_with_yandex(browser):
#     "Проверка перехода на страницу авторизации внешнего приложения - Yandex"
#     auth_page = SearchHelper(browser)
#     auth_page.go_to_site()
#     auth_page.click_to_icon_yandex()
#     assert 'https://oauth.yandex.ru/authorize' in browser.current_url
    #TODO проверить почему не переходит на страницу яндекса


@pytest.mark.parametrize("word", ['Alina', 'П', 'ПолинаИвановаСергеевна242628301'])
def test_validation_name(browser, word):
    "Проверка валидации поля 'Имя' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_firstname(word)
    auth_page.click_button_sing_up()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_HINT_NAME)
    assert element_hint_message.is_displayed()


@pytest.mark.parametrize("word", ['Pushkina', 'П', 'ПолинаИвановаСергеевна242628301'])
def test_validation_last_name(browser, word):
    "Проверка валидации поля 'Фамилия' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_lastname(word)
    auth_page.click_button_sing_up()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_HINT_SURNAME)
    assert element_hint_message.is_displayed()


@pytest.mark.parametrize("word", ['12894638910', '@mail.com', '12ivanov@.ru', '+7918$579777', '9'])
def test_validation_email(browser, word):
    "Проверка валидации поля 'E-mail или мобильный телефон' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_email(word)
    auth_page.click_button_sing_up()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_HINT_EMAIL)
    assert element_hint_message.is_displayed()


# def test_change_user_lastname(browser):
#     "Проверить что при изменении Фамилии пользователя данные сохранятся"
#     auth_page = SearchHelper(browser)
#     auth_page.go_to_site()
#     auth_page.enter_username('89180782555')
#     auth_page.enter_password('Bondareva12')
#     auth_page.click_on_the_button_entry()
#     user_data = auth_page.find_element(SearchLocator.LOCATOR_BUTTON_CHANGE_USER_DATA)
#     user_data.click()
#     time.sleep(5)
    #TODO не удается создать переменную с помощью которой потом работать со страницей учета данных пользователя


def test_password_recovery(browser):
    "Проверить переход на страницу Восстановления пароля"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_button_forgot_password()
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials' in browser.current_url


def test_validation_password_recovery_page(browser):
    "Проверить что невозможно восстановить пароль при вводе валидного логина, но без ввода captcha"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_button_forgot_password()
    auth_page.enter_username('89180782555')
    auth_page.click_button_continue()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_ERROR_MESSAGE)
    assert element_hint_message.is_displayed()


def test_return_to_auth_page(browser):
    "Проверить возвращение на страницу Авторизации из страницы Восстановления пароля"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_button_forgot_password()
    auth_page.click_button_return()
    element = auth_page.find_element(SearchLocator.LOCATOR_TITLE_AUTH)
    assert element.is_displayed()


def test_page_help_from_password_recovery_page(browser):
    "Проверить окрытие страницы Помощь из страницы Восстановление пароля"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_button_forgot_password()
    help_page = auth_page.linking_text_help()
    element = help_page.find_element(By.XPATH, "//h1[contains(text(),'Ваш безопасный ключ к сервисам')]")
    assert element.is_displayed()


def test_return_to_auth_page_from_help_page(browser):
    "Проверить возвращение на страницу авторизации из страницы Помощь"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.linking_text_help()
    auth_page.click_return_to_auth_page()
    element = auth_page.find_element(SearchLocator.LOCATOR_TITLE_AUTH)
    assert element.is_displayed()


def test_help_page_from_register_page(browser):
    "Переход на страницу Помощь со страницы Регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    help_page = auth_page.linking_text_help()
    element = help_page.find_element(By.XPATH, "//h1[contains(text(),'Ваш безопасный ключ к сервисам')]")
    assert element.is_displayed()


def test_user_agreement_page_from_register_page(browser):
    "Проверка перехода на страницу Пользовательского соглашения из страницы Регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.go_to_user_agreemenrs()
    for window_handle in browser.window_handles:
        if window_handle != browser.current_window_handle:
            browser.switch_to.window(window_handle)
            break
    assert browser.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


@pytest.mark.parametrize("word", ['12894638910', 'bondareva', 'П'])
def test_validation_password(browser, word):
    "Проверка валидации поля 'Пароль' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_password(word)
    auth_page.click_button_sing_up()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_HINT_PASSWORD)
    assert element_hint_message.is_displayed()


@pytest.mark.parametrize("word", ['12894638910', 'bondareva', 'П'])
def test_validation_password(browser, word):
    "Проверка валидации поля 'Подтверждение пароля' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_password_confirm(word)
    auth_page.click_button_sing_up()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_HINT_PASSWORD)
    assert element_hint_message.is_displayed()


@pytest.mark.parametrize("password, password_confirm", (['12894638910', 'П'], ['Bondareva1', 'Bondareva2']))
def test_password_and_password_confirm_is_different(browser, password, password_confirm):
    "Проверка валидации поля 'Подтверждение пароля' при регистрации"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.go_to_page_sing_up()
    auth_page.enter_password(password)
    auth_page.enter_password_confirm(password_confirm)
    auth_page.click_button_sing_up()
    element_hint_message = auth_page.find_element(SearchLocator.LOCATOR_HINT_PASSWORD)
    assert element_hint_message.is_displayed()


# def test_checkbox_remember_the_password(browser):
#     "Проверить Запоминание пароля с использование чек-бокса"
#     auth_page = SearchHelper(browser)
#     auth_page.go_to_site()
#     auth_page.enter_username('89180782555')
#     auth_page.enter_password('Bondareva12')
#     auth_page.checkbox_is_selected()
#     auth_page.click_on_the_button_entry()
#     auth_page.click_button_log_out()
#     # auth_page.cli
#     time.sleep(2)
#     # filled_login_field = auth_page.find_element()
#     # assert
#TODO не удалось реализовать, т.к. тест проходит в режиме инкогнито и при выходе не сохраняются данные.
# Тогда вопрос - как реализовать проверку для данного функционала?


def test_auth_with_mail(browser):
    "Проверка перехода на страницу авторизации внешнего приложения - Mail.ru"
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_to_icon_mail()
    time.sleep(2)
    assert 'https://connect.mail.ru/oauth/authorize' in browser.current_url
