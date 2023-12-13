from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button1 = browser.find_element_by_id("book")
    price1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1.click()

    x = browser.find_element_by_id("input_value").text
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))

    butSubmit = browser.find_element_by_id("solve")
    butSubmit.click()

finally:
    time.sleep(7)
    browser.quit()
