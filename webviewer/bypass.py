from selenium.common import WebDriverException


def ensure_click(driver, element):
    try:
        element.click()
    except WebDriverException:
        driver.execute_script("arguments[0].click();", element)