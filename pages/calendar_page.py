import time
from .base_page import BasePage
from ._locators import CalendarBaseLocators, CalendarPageLocators


class CalendarPage(BasePage):
    def should_be_calendar_page(self):
        assert self.is_element_present(*CalendarBaseLocators.HEADER), 'There\'s no header at the calendar page'
        assert self.is_element_present(*CalendarPageLocators.CALENDAR_TOOLBAR), 'There\'s no CALENDAR_TOOLBAR at the calendar page'
        assert self.is_element_present(*CalendarPageLocators.CALENDAR_CONTENT), 'There\'s no CALENDAR_CONTENT at the calendar page'
        assert self.is_element_present(*CalendarPageLocators.SIDEBAR_DATEPICKER), 'There\'s no SIDEBAR_DATEPICKER at the calendar page'
        assert self.is_element_present(*CalendarPageLocators.SIDEBAR_CALENDAR_LIST), 'There\'s no SIDEBAR_CALENDAR_LIST at the calendar page'
        assert self.is_element_present(*CalendarPageLocators.SIDEBAR_FILTER), 'There\'s no SIDEBAR_FILTER at the calendar page'
        assert self.is_element_present(*CalendarPageLocators.SIDEBAR_ABOUT), 'There\'s no SIDEBAR_ABOUT at the calendar page'

    def go_to_list_view(self):
        self.driver.find_element(*CalendarPageLocators.CALENDAR_TOOLBAR_LIST_BTN).click()

    def open_add_event_popup(self):
        self.driver.find_element(*CalendarPageLocators.CALENDAR_ADD_EVENT_BTN).click()
        assert self.is_element_present(*CalendarPageLocators.MODAL_EVENTEDITOR), 'Modal event editor is not presented'



