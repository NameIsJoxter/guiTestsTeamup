import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.calendar_page import CalendarPage


@pytest.fixture()
def authorized(driver, login="quellik+881@gmail.com", password="1йфясву3"):
    LoginPage(driver, 'https://teamup.com/login').open()
    LoginPage(driver, 'https://teamup.com/login').login_user(login, password)
    DashboardPage(driver, driver.current_url).go_to_calendar_page()
    page = CalendarPage(driver, driver.current_url)
    page.should_be_calendar_page()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
