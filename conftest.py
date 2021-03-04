import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    print(f"\nStart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()
