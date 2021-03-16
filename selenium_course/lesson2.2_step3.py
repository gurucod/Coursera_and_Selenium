from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element_by_id("num1")
    num1Eqal = num1.text
    num2 = browser.find_element_by_id("num2")
    num2Eqal = num2.text

    x = str(int(num1Eqal) + int(num2Eqal))



    selector = Select(browser.find_element_by_tag_name("select"))
    #selector.select_by_visible_text(x)  можно искать и так - это по тексту внутри
    selector.select_by_value(x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(5)
    browser.quit()
