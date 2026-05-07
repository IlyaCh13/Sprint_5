from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, RegisterPageLocators
from data import UserData, ExpectedTexts
from helpers import (
    submit_registration_form,
    submit_registration_form_invalid_email,
    submit_registration_form_existing_user,
    generate_unique_email,
    DEFAULT_TIMEOUT,
)


class TestRegistration:

    def test_success_registration(self, driver):
        submit_registration_form(driver, email=generate_unique_email())

        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.text_to_be_present_in_element(
                MainPageLocators.USER_NAME,
                ExpectedTexts.USER_NAME_PART,
            )
        )

    def test_registration_invalid_email(self, driver):
        submit_registration_form_invalid_email(driver)

        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.text_to_be_present_in_element(
                RegisterPageLocators.ERROR_MESSAGE,
                ExpectedTexts.REGISTRATION_ERROR,
            )
        )

    def test_registration_existing_user(self, driver):
        submit_registration_form_existing_user(driver)

        assert WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.text_to_be_present_in_element(
                RegisterPageLocators.ERROR_MESSAGE,
                ExpectedTexts.REGISTRATION_ERROR,
            )
        )