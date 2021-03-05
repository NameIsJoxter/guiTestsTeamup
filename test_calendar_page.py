import pytest
import time

from pages.login_page import LoginPage
from pages.calendar_page import CalendarPage
from pages.dashboard_page import DashboardPage


class TestUserCanCreateEvent:
    @pytest.fixture(scope='function', autouse=True)
    def test_setup(self, driver):
        LoginPage(driver, 'https://teamup.com/login').open()
        LoginPage(driver, 'https://teamup.com/login').login_user('quellik+881@gmail.com', '1йфясву3')
        DashboardPage(driver, driver.current_url).go_to_calendar_page()
        page = CalendarPage(driver, driver.current_url)
        page.should_be_calendar_page()

    def test_user_can_open_add_event_popup(self, driver):
        page = CalendarPage(driver, driver.current_url)
        page.go_to_list_view()
        page.open_add_event_popup()

    @pytest.mark.lastone
    def test_user_can_add_event(self, driver):
        page = CalendarPage(driver, driver.current_url)
        page.go_to_list_view()
        page.open_add_event_popup()
