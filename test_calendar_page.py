import pytest
import time, datetime

from pages.login_page import LoginPage
from pages.calendar_page import CalendarPage
from pages.dashboard_page import DashboardPage


class TestUserCanCreateEvent:
    def test_user_can_open_add_event_popup(self, driver, authorized):
        page = CalendarPage(driver, driver.current_url)
        page.go_to_list_view()
        page.open_add_event_popup_by_btn()

    def test_user_can_add_event(self, driver, authorized):
        page = CalendarPage(driver, driver.current_url)
        page.go_to_list_view()
        page.open_add_event_popup_by_btn()
        page.fill_event_title("Good Old Event")
        page.fill_event_calendar()
        page.click_save_btn()
        page.should_be_success_toast()

    @pytest.mark.needs_review
    def test_user_can_see_added_event(self, driver, authorized):
        date = (datetime.datetime.now() + datetime.timedelta(1)).strftime("%Y-%m-%d")
        title = "Good Old Event"
        page = CalendarPage(driver, driver.current_url)
        # page.open_add_event_popup_by_link()
        # page.fill_event_title(title)
        # page.uncheck_all_day_checkbox()
        # page.fill_event_calendar()
        # page.click_save_btn()
        page.go_to_week_view()
        # Вместо ассерта, функция find_event_at_the_week_view теперь просто возвращает .is_present (true|false)
        assert page.find_event_by_title(driver, title), f'Event is not presented. Date: {date}: title: {title}'


def test_event_creation(driver, authorized):
    # Готовим тестовые данные.
    test_event_title = "Some Random Name"
    calendar_page = CalendarPage(driver, driver.current_url)
    # Создаем ивент.
    calendar_page.create_calendar_event_with_data(title=test_event_title)
    calendar_page.go_to_week_view()
    # Проверяем наличие ивента.
    assert calendar_page.find_event_by_title(driver, test_event_title), \
        f'Unable to find event with title: {test_event_title}'
