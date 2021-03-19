from selenium import webdriver
import unittest
import time


class TestReg(unittest.TestCase):
    def test_reg_pass(self):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Регистрация не прошла. Текст не совпадает")


# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/registration1.html")
#
# input1 = browser.find_element_by_css_selector("div.first_block input.first")
# input1.send_keys("Name")
#
# input1 = browser.find_element_by_css_selector("div.first_block input.first")
# input1.send_keys("traTATATA")
#
# input2 = browser.find_element_by_css_selector("div.first_block input.second")
# input2.send_keys("123")
#
# input3 = browser.find_element_by_css_selector("div.first_block input.third")
# input3.send_keys("Adwdawd@mail.tt")
#
# time.sleep(2)
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
#
# time.sleep(1)
# welcome_text_elt = browser.find_element_by_tag_name("h1")
# welcome_text = welcome_text_elt.text

if __name__ == "__main__":
    unittest.main()