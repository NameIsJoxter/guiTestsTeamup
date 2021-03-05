from .base_page import BasePage
from ._locators import CalendarCreatePagesLocators


class CalendarCreatePage(BasePage):
    link = 'https://teamup.com/calendars'

    def should_be_create_calendar_page(self):
        assert self.is_element_present(*CalendarCreatePagesLocators.CREATE_TITLE), 'There\'s no title at the create page'
        assert self.is_element_present(*CalendarCreatePagesLocators.CREATE_FORM), 'There\'s no create calendar form at the page'
        assert self.driver.find_element(*CalendarCreatePagesLocators.CREATE_TITLE).text == 'Create a Calendar', 'Smth went wrong with the title at the create page'

    def create_calendar(self, title):
        self.driver.find_element(*CalendarCreatePagesLocators.NAME_INPUT).send_keys(title)
        self.driver.find_element(*CalendarCreatePagesLocators.TERMS_CHECKBOX).click()
        self.driver.find_element(*CalendarCreatePagesLocators.CREATE_BTN).click()

    def should_be_success_creation_page(self):
        assert self.is_element_present(*CalendarCreatePagesLocators.SUCCESS_TITLE), 'There\'s no title at the success creation page'
        assert self.driver.find_element (*CalendarCreatePagesLocators.SUCCESS_TITLE).text == 'Your new calendar is ready!', 'Smth went wrong with the title at the success creation page'

    def go_to_calendar_page(self):
        self.driver.find_element(*CalendarCreatePagesLocators.OPEN_CALENDAR_BTN).click()

    def go_to_dashboard_page(self):
        self.driver.find_element(*CalendarCreatePagesLocators.DASHBOARD_BTN).click()
