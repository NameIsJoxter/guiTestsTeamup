import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    print(f"\nStart browser for test")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\nquit browser..")
    driver.quit()
