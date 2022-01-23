"""Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
заповнити і відправити її.
Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
В репозиторії скріншоти зберегти."""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def chrome_table():
    link = "https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link"

    driver = webdriver.Chrome()
    driver.get(link)
    input_name = WebDriverWait(driver, 1).until(
        expected_conditions.element_to_be_clickable((
            By.CSS_SELECTOR, 'input[class="quantumWizTextinputPaperinputInput exportInput"]')))
    input_name.click()
    input_name.send_keys('Олександр')
    driver.save_screenshot('completed_form.png')
    button = driver.find_element(
        By.CSS_SELECTOR, 'span[class="appsMaterialWizButtonPaperbuttonContent exportButtonContent"]')
    button.click()
    driver.save_screenshot('sent_form.png')


if __name__ == "__main__":
    chrome_table()
