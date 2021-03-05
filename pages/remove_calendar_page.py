from .base_page import BasePage
from ._locators import CalendarRemovePagesLocators


class RemoveCalendarPage(BasePage):
    def should_be_remove_calendar_page(self):
        assert self.is_element_present(*CalendarRemovePagesLocators.PASSWORD_INPUT), 'There\'s no password input at the remove calendar page'
        assert self.is_element_present(*CalendarRemovePagesLocators.KEEP_BTN),  'There\'s no keep btn at the remove calendar page'
        assert self.is_element_present(*CalendarRemovePagesLocators.REMOVE_BTN), 'There\'s no remove btn at the remove calendar page'
