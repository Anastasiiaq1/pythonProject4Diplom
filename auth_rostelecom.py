from selenium.webdriver import ActionChains

from base import BasePage
from selenium.webdriver.common.by import By


class SearchLocator:
    LOCATOR_USERNAME = (By.ID, "username")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    LOCATOR_BUTTON_ENTRY = (By.ID, "kc-login")
    LOCATOR_USER = (By.CSS_SELECTOR, '[title="Бондарева Анастасия"]')
    LOCATOR_ERROR_MESSAGE = (By.ID, "form-error-message")
    LOCATOR_BUTTON_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_BUTTON_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_USER_AGREEMENTS_PAGE = (By.ID, "rt-auth-agreement-link")
    LOCATOR_BUTTON_HELP = (By.LINK_TEXT, "Помощь")
    LOCATOR_BUTTON_REGISTER = (By.ID, "kc-register")
    LOCATOR_FIRSTNAME = (By.XPATH, "//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange'"
                                   "and @name='firstName']")
    LOCATOR_BUTTON_SING_UP = (By.XPATH,
                              "//button[@class="
                              "'rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']")
    LOCATOR_LASTNAME = (By.XPATH, "//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange'"
                                  "and @name='lastName']")
    LOCATOR_HINT_NAME = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    LOCATOR_HINT_SURNAME = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
    LOCATOR_HINT_EMAIL = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]')
    LOCATOR_HINT_PASSWORD = (By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')
    LOCATOR_EMAIL = (By.ID, "address")
    LOCATOR_BUTTON_CHANGE_USER_DATA = (By.XPATH, "//button[@class='Вrt-btn rt-btn--orange rt-btn--small rt-btn--rounded"
                                                 " rt-btn--transparent rt-btn--icon base-icon-btn edit-btn edit-btn']")
    # LOCATOR_ICON_YANDEX = (By.ID, "oidc_ya")
    LOCATOR_ICON_MAIL = (By.ID, "oidc_mail")
    LOCATOR_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_BUTTON_CONTINUE = (By.ID, "reset")
    LOCATOR_RESET_BACK = (By.ID, "reset-back")
    LOCATOR_TITLE_AUTH = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    LOCATOR_ENTER_WITH_POSTELEKOM = (By.ID, "faq-close")
    # LOCATOR_CHECKBOX_REMEMBER_PASSWORD = (By.XPATH, "//span[@class='rt-checkbox__shape rt-checkbox__shape--rounded "
    #                                                 "rt-checkbox__shape--orange']")
    # LOCATOR_LOG_OUT = (By.ID, "logout-btn")



class SearchHelper(BasePage):

    def enter_username(self, word):
        "Заполнение поля username"
        username_field = self.find_element(SearchLocator.LOCATOR_USERNAME)
        username_field.click()
        username_field.send_keys(word)
        return username_field

    def enter_password(self, word):
        "Заполнение поля password"
        password_field = self.find_element(SearchLocator.LOCATOR_PASSWORD)
        password_field.click()
        password_field.send_keys(word)
        return password_field

    def enter_password_confirm(self, word):
        "Заполнение поля Подтверждение пароля"
        password_field = self.find_element(SearchLocator.LOCATOR_PASSWORD_CONFIRM)
        password_field.click()
        password_field.send_keys(word)
        return password_field

    def click_on_the_button_entry(self):
        "Вход на страницу учетных данных пользователя"
        return self.find_element(SearchLocator.LOCATOR_BUTTON_ENTRY).click()

    def check_user_page(self):
        "Проверка страницы учетных данных пользователя"
        return self.find_element(SearchLocator.LOCATOR_USER)

    def check_error_auth_message(self):
        "Проверка сообщения об ошибке авторизации"
        return self.find_element(SearchLocator.LOCATOR_ERROR_MESSAGE)

    def click_email_entry(self):
        "Переход на авторизацию с использованием почты"
        return self.find_element(SearchLocator.LOCATOR_BUTTON_EMAIL).click()

    def click_login_entry(self):
        "Переход на авторизацию с использованием логина"
        return self.find_element(SearchLocator.LOCATOR_BUTTON_LOGIN).click()

    def go_to_user_agreemenrs(self):
        "Переход на страницу Пользовательского соглашения"
        user_agreement = self.find_element(SearchLocator.LOCATOR_USER_AGREEMENTS_PAGE)
        user_agreement.click()
        return user_agreement

    def linking_text_help(self):
        "Переход на страницу Помощь"
        help_page = self.find_element(SearchLocator.LOCATOR_BUTTON_HELP)
        ActionChains(self).scroll_to_element(help_page)
        help_page.click()
        return help_page

    def go_to_page_sing_up(self):
        "Переход на страницу регистрации"
        register_page = self.find_element(SearchLocator.LOCATOR_BUTTON_REGISTER)
        register_page.click()
        return register_page

    def enter_firstname(self, word):
        "Заполнение поля Имя при регистрации"
        firstname_field = self.find_element(SearchLocator.LOCATOR_FIRSTNAME)
        firstname_field.click()
        firstname_field.send_keys(word)
        return firstname_field

    def click_button_sing_up(self):
        "Нажатие на кнопку Зарегистрироваться"
        register_button = self.find_element(SearchLocator.LOCATOR_BUTTON_SING_UP)
        register_button.click()
        return register_button

    def enter_lastname(self, word):
        "Заполнение поля Фамилия при регистрации"
        lastname_field = self.find_element(SearchLocator.LOCATOR_LASTNAME)
        lastname_field.click()
        lastname_field.send_keys(word)
        return lastname_field

    def enter_email(self, word):
        "Заполнение поля 'E-mail или мобильный телефон' при регистрации"
        email_field = self.find_element(SearchLocator.LOCATOR_EMAIL)
        email_field.click()
        email_field.send_keys(word)
        return email_field

    # def click_to_icon_yandex(self):
    #     "Нажатие на иконку Yandex"
    #     icon_yandex = self.find_element(SearchLocator.LOCATOR_ICON_YANDEX)
    #     icon_yandex.click()

    def click_to_icon_mail(self):
        "Нажатие на иконку Mail"
        icon_mail = self.find_element(SearchLocator.LOCATOR_ICON_MAIL)
        icon_mail.click()

    def click_button_forgot_password(self):
        "Нажатие на кнопку Забыл пароль"
        linking_text_forgot_password = self.find_element(SearchLocator.LOCATOR_FORGOT_PASSWORD)
        linking_text_forgot_password.click()

    def click_button_continue(self):
        "Нажатие на кнопку продолжить на странице Востановление пароля"
        button_continue = self.find_element(SearchLocator.LOCATOR_BUTTON_CONTINUE)
        button_continue.click()

    def click_button_return(self):
        "Нажатие на кнопку продолжить на странице Востановление пароля"
        button_continue = self.find_element(SearchLocator.LOCATOR_RESET_BACK)
        button_continue.click()

    def click_return_to_auth_page(self):
        "Нажание на кнопку 'Войти с Ростелеком ID' из страницы Помощь"
        return_button = self.find_element(SearchLocator.LOCATOR_ENTER_WITH_POSTELEKOM)
        ActionChains(self).scroll_to_element(return_button)
        return_button.click()
        return return_button

    # def checkbox_is_selected(self):
    #     "Отметка в чек-боксе Запомнить пароль"
    #     checkbox_remember_password = self.find_element(SearchLocator.LOCATOR_CHECKBOX_REMEMBER_PASSWORD)
    #     if checkbox_remember_password.is_selected():
    #         checkbox_remember_password.click()

    # def click_button_log_out(self):
    #     "Нажатие на кнопку Выход"
    #     button_log_out = self.find_element(SearchLocator.LOCATOR_LOG_OUT)
    #     button_log_out.click()
