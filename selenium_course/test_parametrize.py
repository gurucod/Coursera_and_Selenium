import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


linkID = [236895, 236896, 236897, 236898,
          236899, 236903, 236904, 236905]


@pytest.mark.parametrize('id', linkID)
def test_find_answer_correct(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    input1 = browser.find_element_by_css_selector("div[class=\"quiz-component ember-view\"] textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    button_send = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"submit-submission\"]"))
        )
    button_send.click()
    response = browser.find_element_by_css_selector("pre[class=\"smart-hints__hint\"]").text

    assert response == "Correct!", f"Ожидаемый текст не совпал. ФР: {response}"
