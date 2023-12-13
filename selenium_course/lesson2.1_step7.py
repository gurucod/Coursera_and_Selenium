from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    img1 = browser.find_element_by_id("treasure")
    imgAtribute = img1.get_attribute("valuex")
    x = imgAtribute
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    time.sleep(2)

    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    time.sleep(2)

    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()

    time.sleep(2)

    buttonSubmit = browser.find_element_by_css_selector("button.btn")
    buttonSubmit.click()

finally:
    time.sleep(5)
    browser.quit()
