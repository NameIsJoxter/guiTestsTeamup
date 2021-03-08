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
    LOGIN_BTN = (By.CSS_SELECTOR, '#_submit')


class DashboardPageLocators:
    DASHBOARD_INTRO = (By.CSS_SELECTOR,'.intro')
    DASHBOARD_CONTENT = (By.CSS_SELECTOR, '.calendar-box-section')
    FIRST_CALENDAR = (By.CSS_SELECTOR, '.calendar-box-content')
    CALENDAR_BY_TITLE = (By.XPATH, './/h4[contains(text(), title)]')
    REMOVE_CALENDAR_BY_TITLE = (By.XPATH, './/h4[contains(text(), title)]/ancestor::div[contains(@class,"calendar-box-content")]//following::*[contains(text(), "Remove")]')
    CREATE_CALENDAR = (By.CSS_SELECTOR, '.create-calendar-box')
    ADD_CALENDAR_BTN = (By.CSS_SELECTOR, '.add-calendar-btn')


class CalendarCreatePagesLocators:
    # includes calendar/created?key
    CREATE_FORM = (By.CSS_SELECTOR,'.form')
    CREATE_TITLE = (By.CSS_SELECTOR, '.user__login-page-content-right > h1')
    NAME_INPUT = (By.CSS_SELECTOR, '#calendar-name')
    TERMS_CHECKBOX = (By.CSS_SELECTOR, '[for="terms-and-conditions-chx"]')
    CREATE_BTN = (By.CSS_SELECTOR, '#calendar-create')
    SUCCESS_TITLE = (By.CSS_SELECTOR, '.user__login-page-content-right > h1')
    OPEN_CALENDAR_BTN = (By.CSS_SELECTOR, '#btn__settings-ok')
    DASHBOARD_BTN = (By.CSS_SELECTOR, '.user__login-page-content-right p:last-of-type a')


class CalendarRemovePageLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR,'#form_password')
    KEEP_BTN = (By.CSS_SELECTOR,'.btn__settings-ok')
    REMOVE_BTN = (By.CSS_SELECTOR, '.btn__settings-remove')


class CalendarPageLocators:
    CALENDAR_TOOLBAR = (By.CSS_SELECTOR, '.calendar-toolbar')
    CALENDAR_TOOLBAR_LIST_BTN = (By.XPATH, './/li[contains(text(), "List")]')
    CALENDAR_TOOLBAR_WEEK_BTN = (By.XPATH, './/li[text() = "Week"]')
    CALENDAR_ADD_EVENT_BTN = (By.CSS_SELECTOR, '.add-event-btn')

    CALENDAR_CONTENT = (By.CSS_SELECTOR, '.calendar-body-content')
    CALENDAR_WEEK_VIEW = (By.CSS_SELECTOR, '.week-view')
    # CALENDAR_WEEK_TODAY_COLUMN = (By.CSS_SELECTOR, '.day-today')
    CALENDAR_WEEK_COLUMN_BY_DATE_EVENT_BY_TITLE = (By.XPATH, './/*[@class="columns"]//div[contains(@data-date, date)]//*[contains(@class, "event")]//*[@class="event-title" and text() = title] ')

    SIDEBAR_DATEPICKER = (By.CSS_SELECTOR, '.sidebar-datepicker')
    SIDEBAR_CALENDAR_LIST = (By.CSS_SELECTOR, '.calendar-list-widget')
    SIDEBAR_FILTER = (By.CSS_SELECTOR, '.filter-widget')
    SIDEBAR_ABOUT = (By.CSS_SELECTOR, '.about-widget')

    MODAL_EVENTEDITOR = (By.CSS_SELECTOR, '.eventeditor')
    MODAL_EVENTEDITOR_TITLE = (By.CSS_SELECTOR, '#title')
    MODAL_EVENTEDITOR_CALENDAR_PLACEHOLDER = (By.CSS_SELECTOR, '.Select-placeholder')
    MODAL_EVENTEDITOR_CALENDAR_INPUT = (By.CSS_SELECTOR, '.calendarpicker .Select-input input')
    MODAL_EVENTEDITOR_ALL_DAY_CHECKBOX = (By.CSS_SELECTOR, '#all_day')
    MODAL_EVENTEDITOR_ALL_DAY_CHECKBOX_LABEL = (By.CSS_SELECTOR, '.all-day-label label')
    MODAL_EVENTEDITOR_SAVE_BTN = (By.CSS_SELECTOR, '.save-button [type=submit]')
    MODAL_EVENTEDITOR_TO_TIME = (By.CSS_SELECTOR, '.date-to-value .select-widget-input')
    SUCCESS_ADD_EVENT_TOAST = (By.CSS_SELECTOR, '.flash-message-enter-done')
