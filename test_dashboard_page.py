from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# class TestUserCreateCalendarFromDashboardPage(BasePage):
#     def test_setup(self, driver):
#         login_page = LoginPage(driver, 'https://teamup.com/login')
#         login_page.open()
#         login_page.login_user('quellik+881@gmail.com', '1йфясву3')
#         page = DashboardPage(driver, driver.current_url)
#         page.should_be_autorized_user()
#         page.should_be_dashboard_page()
#
#     def test_create_calendar(self, driver):
