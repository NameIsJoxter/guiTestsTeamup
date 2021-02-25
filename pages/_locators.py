from selenium.webdriver.common.by import By


class CalendarBaseLocators:
    HEADER = (By.CSS_SELECTOR, '.calendar-header')
    TITLE = (By.CSS_SELECTOR, '.title')
    NEWS_ICON = (By.CSS_SELECTOR, '#news_ticker')
    USER_ICON = (By.CSS_SELECTOR, '#user-avatar')
    FOOTER = (By.CSS_SELECTOR, '.footer-page')


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '#username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    # REMEMBER_ME_CHECKBOX
    LOGIN_BTN = (By.CSS_SELECTOR, '#_submit')


class DashboardPageLocators:
    DASHBOARD_INTRO = (By.CSS_SELECTOR,'.intro')
    DASHBOARD_CONTENT = (By.CSS_SELECTOR, '.calendar-box-section')
    # FIRST_CALENDAR = (By.CSS_SELECTOR,'.calendar-box-content:first-of-type')
    # REMOVE_FIRST_CALENDAR = (By.CSS_SELECTOR, '.calendar-box-content:first-of-type .dashboard-remove-calendar')
    CREATE_CALENDAR_DIV = (By.CSS_SELECTOR, '.create-calendar-box')
    ADD_CALENDAR_BTN = (By.CSS_SELECTOR, '.add-calendar-btn')


class CalendarCreatePagesLocators:
    # includes calendar/created?key
    CREATE_TITLE = (By.CSS_SELECTOR, '.user__login - page - content - right > h1')
    NAME_INPUT = (By.CSS_SELECTOR, '#calendar-name')
    TERMS_CHECKBOX = (By.CSS_SELECTOR, '#terms-and-conditions-chx')
    CREATE_BTN = (By.CSS_SELECTOR, '#calendar-create')
    SUCCESS_TITLE = (By.CSS_SELECTOR, '.user__login-page-content-right > h1')
    OPEN_CALENDAR_BTN = (By.CSS_SELECTOR, '#btn__settings-ok')
    DASHBOARD_BTN = (By.CSS_SELECTOR, '.user__login-page-content-right p:last-of-type a')

