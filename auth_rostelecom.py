from selenium.webdriver import ActionChains

from base import BasePage
from selenium.webdriver.common.by import By


class SearchLocator:
    LOCATOR_USERNAME = (By.ID, "username")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_BUTTON_ENTRY = (By.ID, "kc-login")
    LOCATOR_USER = (By.CSS_SELECTOR, '[title="Бондарева Анастасия"]')
    LOCATOR_ERROR_MESSAGE = (By.ID, "form-error-message")
    LOCATOR_BUTTON_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_USER_AGREEMENTS_PAGE = (By.ID, "rt-auth-agreement-link")
    # LOCATOR_BUTTON_HELP = (By.CLASS_NAME, "rt-link rt-link--orange faq-modal-tip__btn")
    LOCATOR_BUTTON_HELP = (By.LINK_TEXT, "Помощь")
    LOCATOR_TEXT_HELP = (By.LINK_TEXT, "Ваш безопасный ключ к сервисам Ростелекома")
    LOCATOR_BUTTON_REGISTER = (By.ID, "kc-register")
    LOCATOR_FIRSTNAME = (By.XPATH, "//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange'"
                                   "and @name='firstName']")
    LOCATOR_BUTTON_SING_UP = (By.XPATH,
                              "//button[@class="
                              "'rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']")
    LOCATOR_LASTNAME = (By.XPATH, "//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange'"
                                  "and @name='lastName']")
    LOCATOR_HINT_NAME = (By.LINK_TEXT, "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")
    LOCATOR_EMAIL = (By.ID, "address")


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

    def go_to_user_agreemenrs(self):
        "Переход на страницу Пользовательского соглашения"
        user_agreement = self.find_element(SearchLocator.LOCATOR_USER_AGREEMENTS_PAGE)
        user_agreement.click()
        return user_agreement

    def open_help_page(self):
        "Переход на страницу Помощь"
        help_page = self.find_element(SearchLocator.LOCATOR_BUTTON_HELP)
        ActionChains(self).scroll_to_element(help_page).perform()
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
