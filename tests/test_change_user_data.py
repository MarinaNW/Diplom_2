
from api_methods import ApiMethods
from helpers import Helper
import pytest
import allure


@allure.title("Тесты на изменение данных авторизованного пользователя")
class TestUpdateUser:

    @allure.title("Тест на изменение email авторизованного пользователя")
    def test_change_user_email(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_email = Helper.generate_email()

        # Регистрация пользователя
        ApiMethods.register_user(email, password, username)

        # Авторизация пользователя
        response= ApiMethods.login_user(email, password)

        # Получаем токен для авторизации
        token = response.json().get('accessToken')

        # Обновление данных пользователя
        update_response=ApiMethods.change_user_email(token, new_email, password, username)
        assert update_response.status_code == 200 and update_response.json()['user']['email'] == new_email

        # Удаление пользователя
        ApiMethods.delete_user(token)

    @allure.title("Тест на изменение имени авторизованного пользователя")
    def test_change_user_email(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_username = Helper.generate_name()

        # Регистрация пользователя
        ApiMethods.register_user(email, password, username)

        # Авторизация пользователя
        response = ApiMethods.login_user(email, password)

        # Получаем токен для авторизации
        token = response.json().get('accessToken')

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, password, new_username)
        assert update_response.status_code == 200 and update_response.json()['user']['name'] == new_username

        # Удаление пользователя
        ApiMethods.delete_user(token)


    @allure.title("Тест на изменение пароля авторизованного пользователя")
    def test_change_user_password(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_password = Helper.generate_password()

        # Регистрация пользователя
        ApiMethods.register_user(email, password, username)

        # Авторизация пользователя
        response = ApiMethods.login_user(email, password)

        # Получаем токен для авторизации
        token = response.json().get('accessToken')

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, new_password, username)
        assert update_response.status_code == 200 and update_response.json()['success'] == True

        # Удаление пользователя
        ApiMethods.delete_user(token)

    @allure.title("Тест на изменение email неавторизованного пользователя")
    def test_change_unauthorized_user_email(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_email = Helper.generate_email()

        # Регистрация пользователя
        response=ApiMethods.register_user(email, password, username)
        token = response.json().get('accessToken')

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_email(token, new_email, password, username)
        assert update_response.status_code == 200 and update_response.json()['user']['email'] == new_email

        # Удаление пользователя
        ApiMethods.delete_user(token)

    @allure.title("Тест на изменение имени неавторизованного пользователя")
    def test_change_unauthorized_user_email(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_username = Helper.generate_name()

        # Регистрация пользователя
        response = ApiMethods.register_user(email, password, username)
        token = response.json().get('accessToken')

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, password, new_username)
        assert update_response.status_code == 200 and update_response.json()['user']['name'] == new_username

        # Удаление пользователя
        ApiMethods.delete_user(token)

    @allure.title("Тест на изменение пароля неавторизованного пользователя")
    def test_change_unauthorized_user_password(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_password = Helper.generate_password()

        # Регистрация пользователя
        response = ApiMethods.register_user(email, password, username)
        token = response.json().get('accessToken')

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, new_password, username)
        assert update_response.status_code == 200 and update_response.json()['success'] == True

        # Удаление пользователя
        ApiMethods.delete_user(token)

    @allure.title("Тест на изменение email пользователя без поля авторизации")
    def test_change_unauthorized_user_email_without_authorization(self):
        # Данные для регистрации пользователя
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()
        new_email = Helper.generate_email()

        # Регистрация пользователя
        ApiMethods.register_user(email, password, username)

        # Обновление данных пользователя
        token=''
        update_response = ApiMethods.change_user_email(token,new_email, password, username)
        assert update_response.status_code == 401 and update_response.json()["message"]== "You should be authorised"



