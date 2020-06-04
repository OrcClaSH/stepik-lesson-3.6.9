from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_contains_add_button_to_basket(browser):
    # Переход по указанной ссылке
    browser.get(
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    )
    # Нахождение кнопки "Добавить в корзину"
    button_basket = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
        )
    )
    # Вывод текста на кнопке
    print('button_text: ', button_basket.text)
    # Дополнительная проверка в виде перехода по кнопке
    button_basket.click()
    # Нахождение кнопок "Посмотреть корзину"
    #  - удостоверимся, что успешно добавили в корзину
    button_view_basket = browser.find_elements_by_css_selector(
        '.alert > div > p:nth-child(2) > a:nth-child(1)'
    )
    # Выполним assert в случае отсутствия кнопки "Посмотреть корзину"
    assert len(button_view_basket) > 0, 'no button see basket'
