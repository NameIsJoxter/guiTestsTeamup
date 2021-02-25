from selenium.common.exceptions import TimeoutException
from ._locators import CalendarBaseLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except TimeoutException:
            return False
        return True

    def should_be_autorized_user(self):
        assert self.is_element_present(*CalendarBaseLocators.USER_ICON), \
            'User icon is not presented, probably unautorized user'
