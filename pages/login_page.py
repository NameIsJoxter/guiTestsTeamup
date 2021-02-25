from .base_page import BasePage
from ._locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def should_be_login_page(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT), 'There\'s no email input at the page'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT),'There\'s no password input at the page'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), 'There\'s no submit button at the page'
