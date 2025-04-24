
from api_methods import ApiMethods
from helpers import Helper
import pytest
import allure


@allure.title("Тесты на создание пользователя")
class TestCreateUser:

    @allure.title("Тест на cоздание уникального пользователя")
    def test_user_registration(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()

        # Регистрация пользователя
        registration_response = ApiMethods.register_user(email, password, username)
        assert registration_response.status_code==200 and registration_response.json()['success'] == True

        # Удаление пользователя
        token_response = ApiMethods.login_user(email, password)
        token = token_response.json().get('accessToken')
        ApiMethods.delete_user(token)

    @allure.title("Тест на возврат ошибки при cоздании зарегистрированного пользователя")
    def test_re_register_user(self,user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        password = user_data['password']
        username = user_data['username']

        # Проверка, что зарегистрированного пользователя нельзя повторно зарегистрировать
        re_register_user = ApiMethods.register_user(email, password, username)
        assert re_register_user.status_code == 403 and re_register_user.json()['message']== "User already exists"

    @allure.title("Тест на возврат ошибки при отсутствии обязательного поля")
    @pytest.mark.parametrize(
        "email, password, username",
        [
            ("", Helper.generate_password(), Helper.generate_name()),
            (Helper.generate_email(), "", Helper.generate_name()),
            (Helper.generate_email(), Helper.generate_password(), "")
        ]
    )
    def test_unsuccessful_registration_without_required_field(self, email, password, username):
        registration_response = ApiMethods.register_user(email, password, username)
        assert registration_response.status_code==403 and registration_response.json()['message'] == "Email, password and name are required fields"




