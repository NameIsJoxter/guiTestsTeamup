import pytest
import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.calendars_page import CalendarsPage
from pages.remove_calendar_page import RemoveCalendarPage


class TestUserCanCreateCalendarFromDashboardPage:
    @pytest.fixture(scope='function', autouse=True)
    def test_setup(self, driver):
        login_page = LoginPage(driver, 'https://teamup.com/login')
        login_page.open()
        login_page.login_user('quellik+881@gmail.com', '1йфясву3')
        page = DashboardPage(driver, driver.current_url)
        page.should_be_autorized_user()

    def test_user_can_open_create_calendar_page(self, driver):
        page = DashboardPage(driver, driver.current_url)
        page.go_to_create_calendar_page()
        page = CalendarsPage(driver, driver.current_url)
        page.should_be_create_calendar_page()

    def test_user_can_create_calendar(self, driver):
        DashboardPage(driver, driver.current_url).go_to_create_calendar_page()
        page = CalendarsPage(driver, CalendarsPage.link)
        page.create_calendar('test calendar')
        page.should_be_success_creation_page()

    def test_user_can_see_new_calendar_at_the_dashboard_page(self, driver):
        title = 'this calendar definitely exists'
        DashboardPage(driver, driver.current_url).go_to_create_calendar_page()
        CalendarsPage(driver, CalendarsPage.link).create_calendar(title)
        CalendarsPage(driver, driver.current_url).go_to_dashboard_page()
        page = DashboardPage(driver, driver.current_url)
        page.calendar_widget_is_visible(title)


class TestUserCanDeleteCalendarFromDashboardPage:
    @pytest.fixture(scope='function', autouse=True)
    def test_setup(self, driver):
        login_page = LoginPage(driver, 'https://teamup.com/login')
        login_page.open()
        login_page.login_user('quellik+881@gmail.com', '1йфясву3')
        page = DashboardPage(driver, driver.current_url)
        page.should_be_autorized_user()

    def test_user_can_go_to_delete_calendar_page(self, driver):
        title = 'brand new calendar'
        DashboardPage(driver, driver.current_url).go_to_create_calendar_page()
        CalendarsPage(driver, CalendarsPage.link).create_calendar(title)
        CalendarsPage(driver, driver.current_url).go_to_dashboard_page()
        page = DashboardPage(driver, driver.current_url)
        page.go_to_remove_calendar_page(title)
        page = RemoveCalendarPage(driver, driver.current_url)
        page.should_be_remove_calendar_page()
