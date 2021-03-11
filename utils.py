import time
from selenium.webdriver.common.by import By


def smart_wait_by_xpath(driver, element_xpath, timeout=20):
    t_end = time.time() + timeout
    while time.time() < t_end:
        search_result = driver.find_elements(By.XPATH, element_xpath)
        if len(search_result) > 0:
            return search_result[0]
        else:
            time.sleep(0.3)
    return None
