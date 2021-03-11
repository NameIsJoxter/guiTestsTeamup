import time, datetime
from selenium.webdriver.common.keys import Keys
from utils import smart_wait_by_xpath

from .base_page import BasePage
from ._locators import CalendarBaseLocators, CalendarPageLocators


class CalendarPage(BasePage):

    def should_be_calendar_page(self):
        assert self.is_element_present(*CalendarBaseLocators.HEADER), 'There\'s no header at the calendar page'
        assert self.is_element_present(
            *CalendarPageLocators.CALENDAR_TOOLBAR), 'There\'s no CALENDAR_TOOLBAR at the calendar page'
        assert self.is_element_present(
            *CalendarPageLocators.CALENDAR_CONTENT), 'There\'s no CALENDAR_CONTENT at the calendar page'
        assert self.is_element_present(
            *CalendarPageLocators.SIDEBAR_DATEPICKER), 'There\'s no SIDEBAR_DATEPICKER at the calendar page'
        assert self.is_element_present(
            *CalendarPageLocators.SIDEBAR_CALENDAR_LIST), 'There\'s no SIDEBAR_CALENDAR_LIST at the calendar page'
        assert self.is_element_present(
            *CalendarPageLocators.SIDEBAR_FILTER), 'There\'s no SIDEBAR_FILTER at the calendar page'
        assert self.is_element_present(
            *CalendarPageLocators.SIDEBAR_ABOUT), 'There\'s no SIDEBAR_ABOUT at the calendar page'

    def go_to_list_view(self):
        self.driver.find_element(*CalendarPageLocators.CALENDAR_TOOLBAR_LIST_BTN).click()

    def go_to_week_view(self):
        self.driver.find_element(*CalendarPageLocators.CALENDAR_TOOLBAR_WEEK_BTN).click()
        assert self.is_element_present(
            *CalendarPageLocators.CALENDAR_WEEK_VIEW), 'Can\'t switch to week view'

    def find_event_at_the_week_view(self, date, title):
        return self.is_element_present(*CalendarPageLocators.CALENDAR_WEEK_COLUMN_BY_DATE_EVENT_BY_TITLE)

    def find_event_by_title(self, driver, title):
        return smart_wait_by_xpath(driver, f"//span[normalize-space()='{title}']")

    def open_add_event_popup_by_btn(self):
        self.driver.find_element(*CalendarPageLocators.CALENDAR_ADD_EVENT_BTN).click()
        assert self.is_element_present(*CalendarPageLocators.MODAL_EVENTEDITOR), 'Modal event editor is not presented'

    def open_add_event_popup_by_link(self):
        add_event_with_start_date_param = '/events/new?start_dt=' + self.today_plus_days(1).strftime("%Y-%m-%d")
        self.driver.get(self.driver.current_url+add_event_with_start_date_param)

    def fill_event_title(self, title):
        self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_TITLE).send_keys(title)

    def uncheck_all_day_checkbox(self):
        checkbox = self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_ALL_DAY_CHECKBOX).get_attribute(
            'value')
        if checkbox == '1':
            self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_ALL_DAY_CHECKBOX_LABEL).click()
        checkbox = self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_ALL_DAY_CHECKBOX).get_attribute(
            'value')
        assert checkbox == '0', 'Expected all day checkbox ' + checkbox + ' to be NOT checked, but it is'

    def fill_event_calendar(self):
        self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_CALENDAR_PLACEHOLDER).click()
        self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_CALENDAR_INPUT).send_keys('1')
        self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_CALENDAR_INPUT).send_keys(Keys.ENTER)

    def click_save_btn(self):
        self.driver.find_element(*CalendarPageLocators.MODAL_EVENTEDITOR_SAVE_BTN).click()

    def should_be_success_toast(self):
        assert self.is_element_present(*CalendarPageLocators.SUCCESS_ADD_EVENT_TOAST), 'There\'s no success toast'

    def create_calendar_event_with_data(self, title):
        self.go_to_list_view()
        self.open_add_event_popup_by_btn()
        self.fill_event_title(title)
        self.fill_event_calendar()
        self.click_save_btn()
        self.should_be_success_toast()
