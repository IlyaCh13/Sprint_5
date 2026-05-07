# Данные для тестов, такие как существующий пользователь, данные для нового объявления и ожидаемые тексты в интерфейсе

class UserData:
    # Данные существующего пользователя
    EXISTING_EMAIL = "testuser@test.com"
    EXISTING_PASSWORD = "Password123"

    # Пароль для регистрации нового пользователя
    NEW_USER_PASSWORD = "Password123"

    # Невалидные данные
    INVALID_EMAIL = "invalid_email"


class AdData:
    TITLE = "Test product"
    DESCRIPTION = "Test description"
    PRICE = "1000"


class ExpectedTexts:
    UNAUTHORIZED_MODAL_TITLE = "Чтобы разместить объявление, авторизуйтесь"
    REGISTRATION_ERROR = "Ошибка"
    USER_NAME_PART = "User"
