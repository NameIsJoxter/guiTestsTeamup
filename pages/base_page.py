from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def move_to_element(self, how, what):
        element = self.driver.find_element(how, what)
        try:
            ActionChains(self.driver).move_to_element_with_offset(element, 0, 0).perform()
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_autorized_user(self):
        assert self.is_element_present(*CalendarBaseLocators.USER_ICON), \
            'User icon is not presented, probably unautorized user'
