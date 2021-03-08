import pytest
import time, datetime

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
        page.open_add_event_popup_by_btn()

    def test_user_can_add_event(self, driver):
        page = CalendarPage(driver, driver.current_url)
        page.go_to_list_view()
        page.open_add_event_popup_by_btn()
        page.fill_event_title()
        page.fill_event_calendar()
        page.click_save_btn()
        page.should_be_success_toast()

    @pytest.mark.needs_review
    def test_user_can_see_added_event(self, driver):
        date = (datetime.datetime.now() + datetime.timedelta(1)).strftime("%Y-%m-%d")
        title = datetime.datetime.now().strftime("%c")
        page = CalendarPage(driver, driver.current_url)
        # page.open_add_event_popup_by_link()
        # page.fill_event_title(title)
        # page.uncheck_all_day_checkbox()
        # page.fill_event_calendar()
        # page.click_save_btn()
        page.go_to_week_view()
        time.sleep(1)
        page.find_event_at_the_week_view(date, title)
        time.sleep(5)

