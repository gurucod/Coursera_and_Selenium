from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_el = browser.find_element_by_id("input_value").text
    y = calc(x_el)


    input1 = browser.find_element_by_css_selector("div.form-group input[type=\"text\"]")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()

    button.click()

finally:
    time.sleep(5)
    browser.quit()