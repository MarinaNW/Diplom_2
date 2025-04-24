from api_methods import ApiMethods
from data import Data
from helpers import Helper
import pytest
import allure


@allure.title("Тесты на создание пользователя")
class TestLoginUser:

    @allure.title("Тест на авторизацию пользователя")
    def test_login_user(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        assert response.status_code == 200 and response.json()['success'] == True
        assert response.json()['user']['email']==Data.email

    @allure.title("Тест на авторизацию пользователя с неверными данными")
    @pytest.mark.parametrize(
        "email, password",
        [
            (Data.email, Helper.generate_name()),
            (Helper.generate_email(), Data.password),
        ]
    )
    def test_unsuccessful_login_user(self,email, password):
        authorization_response = ApiMethods.login_user(email, password)
        assert authorization_response.status_code == 401 and authorization_response.json()['message'] == "email or password are incorrect"

