from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    input1 = browser.find_element_by_css_selector("div.first_block input.first")
    input1.send_keys("traTATATA")
    input2 = browser.find_element_by_css_selector("div.first_block input.second")
    input2.send_keys("123")
    input3 = browser.find_element_by_css_selector("div.first_block input.third")
    input3.send_keys("Adwdawd@mail.tt")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
