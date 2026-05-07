from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators
from data import ExpectedTexts
from helpers import login, DEFAULT_TIMEOUT


class TestLogin:

    def test_login(self, driver):
        login(driver)

        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(        # Ждём появления имени пользователя в шапке после успешного входа
            EC.text_to_be_present_in_element(
                MainPageLocators.USER_NAME,
                ExpectedTexts.USER_NAME_PART,
            )
        )
