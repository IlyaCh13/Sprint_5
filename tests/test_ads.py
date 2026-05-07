from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ModalLocators, SearchResultsLocators
from data import AdData, ExpectedTexts
from helpers import (
    open_main_page,
    login,
    fill_and_publish_ad,
    search_ad_by_title,
)
from helpers import DEFAULT_TIMEOUT
from locators import MainPageLocators


class TestAds: # Тесты, связанные с созданием и отображением объявлений

    def test_create_ad_unauthorized(self, driver):
        open_main_page(driver)
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()     # Нажимаем кнопку "Разместить объявление" без авторизации

        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(        # Ждём появления модалки с требованием авторизации
            EC.text_to_be_present_in_element(
                ModalLocators.AUTH_REQUIRED_TITLE,
                ExpectedTexts.UNAUTHORIZED_MODAL_TITLE,
            )
        )

    def test_create_ad_authorized(self, driver):
        login(driver)
        fill_and_publish_ad(driver)
        search_ad_by_title(driver, AdData.TITLE)

        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(        # Ждём появления карточки объявления с нашим названием в результатах поиска
            EC.visibility_of_element_located(
                (By.XPATH, SearchResultsLocators.AD_CARD_BY_TITLE.format(AdData.TITLE))
            )
        )