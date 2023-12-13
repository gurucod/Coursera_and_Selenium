from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button1 = browser.find_element_by_css_selector("button.trollface")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))

    butSubmit = browser.find_element_by_css_selector("button.btn")
    butSubmit.click()

finally:
    time.sleep(7)
    browser.quit()
