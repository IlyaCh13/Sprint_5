from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Я хочу купить...']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Применить')]")


class AuthPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_LINK = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")


class RegisterPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    REPEAT_PASSWORD = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(text(),'Ошибка')]")


class ModalLocators:
    AUTH_REQUIRED_TITLE = (By.XPATH,"//div[contains(@class,'modal')]//h1[contains(text(),'авторизуйтесь')]")


class AdFormLocators:
    TITLE_INPUT = (By.XPATH, "//input[@name='name']")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_OPTION_FIRST = (By.XPATH, "//div[contains(@class,'dropDownMenu_options')]//button[1]")
    CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION_FIRST = (
        By.XPATH,
        "//input[@name='city']/ancestor::div[contains(@class,'dropDownMenu_dropMenu')]"
        "//div[not(contains(@class,'_hidden'))]//button[1]",
    )
    CONDITION_RADIO_NEW = (By.XPATH,"//input[@name='condition'][@value='Новый']/parent::div[contains(@class,'radioUnput_shell')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Опубликовать')]")


class SearchResultsLocators:
    AD_CARD_BY_TITLE = "//h2[@class='h2' and text()='{}']"
