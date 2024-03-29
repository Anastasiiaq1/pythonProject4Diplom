from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/auth"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      f'Не удается найти элемент с локатором{locator}')

    def go_to_site(self):
        return self.driver.get(self.base_url)
