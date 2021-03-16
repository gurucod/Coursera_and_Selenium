from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element_by_css_selector("input#robotCheckbox")
    checkbox1.click()

    radButton1 = browser.find_element_by_css_selector("[for='robotsRule']")
    radButton1.click()

    buttonSend = browser.find_element_by_css_selector("button[type=\"submit\"]")
    buttonSend.click()

finally:
    time.sleep(10)
    browser.quit()
