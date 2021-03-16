from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://192.168.11.120/")

    button1 = browser.find_element_by_xpath("//a[text()=\"Войти\"]")
    button1.click()

    time.sleep(2)

    input1 = browser.find_element_by_css_selector("#app input[id=\"id_username\"]")
    input1.send_keys("Stud1@ya.ru")
    input2 = browser.find_element_by_css_selector("#app input[id=\"id_password\"]")
    input2.send_keys("1qwe2qaz")

    time.sleep(3)

    button2 = browser.find_element_by_css_selector("button.waves-effect")
    button2.click()

    text_message = browser.find_element_by_tag_name("blockquote")
    text_error = text_message.text

#    assert "Пожалуйста, введите правильные адрес электронной почты и пароль. Оба поля могут быть чувствительны к регистру." == text_error
#    print("Fail")



finally:
    time.sleep(3)
    browser.quit()
