from selenium import webdriver
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    inputFname = browser.find_element_by_css_selector("input[name=\"firstname\"]")
    inputFname.send_keys("WADWADWD")

    inputLname = browser.find_element_by_css_selector("input[name=\"lastname\"]")
    inputLname.send_keys("Fsdfsfsf")

    inputMail = browser.find_element_by_css_selector("input[name=\"email\"]")
    inputMail.send_keys('awdwad@wdwad.ru')

    downLoad = browser.find_element_by_id("file")
    downLoad.send_keys(file_path)

    buttonSubmit = browser.find_element_by_css_selector("button.btn")
    buttonSubmit.click()

finally:
    time.sleep(8)
    browser.quit()

