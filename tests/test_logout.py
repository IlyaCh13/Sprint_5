from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators
from helpers import login, DEFAULT_TIMEOUT


class TestLogout:

    def test_logout(self, driver):
        # Предусловие: пользователь авторизован
        login(driver)

        driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()        # Нажимаем кнопку "Выйти"

        # Ожидание появления кнопки входа — единственное взаимодействие
        # с маркером успеха, выполняется внутри ассерта
        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
