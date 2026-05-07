import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, AuthPageLocators, AdFormLocators, RegisterPageLocators
from data import UserData, AdData
from urls import Urls, Endpoints

DEFAULT_TIMEOUT = 10


def generate_unique_email():
    return f"user_{int(time.time())}@test.com"


def open_main_page(driver):
    driver.get(Urls.BASE_URL + Endpoints.MAIN_PAGE)


def login(driver):
    open_main_page(driver)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)
    ).send_keys(UserData.EXISTING_EMAIL)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MainPageLocators.USER_NAME)
    )


def open_registration_form(driver):
    open_main_page(driver)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AuthPageLocators.REGISTER_LINK)
    ).click()


def submit_registration_form(driver, email):
    open_registration_form(driver)
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    ).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(UserData.NEW_USER_PASSWORD)
    driver.find_element(*RegisterPageLocators.REPEAT_PASSWORD).send_keys(UserData.NEW_USER_PASSWORD)
    driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()


def submit_registration_form_invalid_email(driver):
    open_registration_form(driver)
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    ).send_keys(UserData.INVALID_EMAIL)
    driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()


def submit_registration_form_existing_user(driver):
    open_registration_form(driver)
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(RegisterPageLocators.EMAIL_INPUT)
    ).send_keys(UserData.EXISTING_EMAIL)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
    driver.find_element(*RegisterPageLocators.REPEAT_PASSWORD).send_keys(UserData.EXISTING_PASSWORD)
    driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()


def fill_and_publish_ad(driver):
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)
    ).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AdFormLocators.TITLE_INPUT)
    ).send_keys(AdData.TITLE)
    driver.find_element(*AdFormLocators.DESCRIPTION_INPUT).send_keys(AdData.DESCRIPTION)
    driver.find_element(*AdFormLocators.PRICE_INPUT).send_keys(AdData.PRICE)
    driver.find_element(*AdFormLocators.CATEGORY_ARROW).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AdFormLocators.CATEGORY_OPTION_FIRST)
    ).click()
    driver.find_element(*AdFormLocators.CITY_ARROW).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AdFormLocators.CITY_OPTION_FIRST)
    ).click()
    driver.find_element(*AdFormLocators.CONDITION_RADIO_NEW).click()
    driver.find_element(*AdFormLocators.PUBLISH_BUTTON).click()


def search_ad_by_title(driver, title):
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(MainPageLocators.SEARCH_INPUT)
    ).send_keys(title)
    driver.find_element(*MainPageLocators.SEARCH_BUTTON).click()