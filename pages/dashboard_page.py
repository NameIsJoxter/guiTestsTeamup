from .base_page import BasePage
from ._locators import CalendarBaseLocators, DashboardPageLocators


class DashboardPage(BasePage):
    def should_be_dashboard_page(self):
        assert self.is_element_present(*DashboardPageLocators.DASHBOARD_INTRO), 'There\'s no dashboard intro at the dashboard page'
        assert self.is_element_present(*DashboardPageLocators.DASHBOARD_CONTENT), 'There\'s no dashboard content at the dashboard page'
        assert self.driver.find_element(*CalendarBaseLocators.TITLE).text == 'Dashboard', 'Title of the dashboard page is not "Dashboard"'
        assert self.is_element_present(*CalendarBaseLocators.HEADER), 'There\'s no header at the dashboard page'
        assert self.is_element_present(*CalendarBaseLocators.FOOTER), 'There\'s no footer input at the dashboard page'

    def go_to_create_calendar_page(self):
        self.driver.find_element(*DashboardPageLocators.CREATE_CALENDAR_DIV).click()

    def calendar_widget_is_visible(self, title):
        assert self.is_element_present(*DashboardPageLocators.CALENDAR_BY_TITLE)

    def go_to_remove_calendar_page(self, title):
        self.move_pointer_to_element(*DashboardPageLocators.CALENDAR_BY_TITLE)
        self.driver.find_element(*DashboardPageLocators.REMOVE_CALENDAR_BY_TITLE).click()
