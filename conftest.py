import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Фикстура для создания и закрытия драйвера, используется во всех тестах
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()
