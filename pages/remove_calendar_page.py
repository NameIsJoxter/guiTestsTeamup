from .base_page import BasePage
from ._locators import CalendarRemovePageLocators


class RemoveCalendarPage(BasePage):
    def should_be_remove_calendar_page(self):
        assert self.is_element_present(*CalendarRemovePageLocators.PASSWORD_INPUT), 'There\'s no password input at the remove calendar page'
        assert self.is_element_present(*CalendarRemovePageLocators.KEEP_BTN), 'There\'s no keep btn at the remove calendar page'
        assert self.is_element_present(*CalendarRemovePageLocators.REMOVE_BTN), 'There\'s no remove btn at the remove calendar page'
