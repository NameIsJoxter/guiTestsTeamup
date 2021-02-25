from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

link = 'https://teamup.com/login'


class TestLogin():
    def test_guest_can_go_to_login_page(self, driver):
        page = LoginPage(driver, link)
        page.open()
        page.should_be_login_page()

    def test_user_can_login(self, driver):
        page = LoginPage(driver, link)
        page.open()
        page.login_user('quellik+881@gmail.com', '1йфясву3')
        dashboard_page = DashboardPage(driver, driver.current_url)
        dashboard_page.should_be_dashboard_page()
        dashboard_page.should_be_autorized_user()
