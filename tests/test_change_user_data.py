from api_methods import ApiMethods
from helpers import Helper
import allure


@allure.title("Тесты на изменение данных авторизованного пользователя")
class TestUpdateUser:

    @allure.title("Тест на изменение email авторизованного пользователя")
    def test_change_user_email(self, user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        password = user_data['password']
        username = user_data['username']
        new_email = Helper.generate_email()
        token = user_data['token']

        ApiMethods.login_user(email, password)

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_email(token, new_email, password, username)
        assert update_response.status_code == 200 and update_response.json()['user']['email'] == new_email


    @allure.title("Тест на изменение имени авторизованного пользователя")
    def test_change_user_name(self, user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        password = user_data['password']
        token = user_data['token']
        new_username = Helper.generate_email()

        # Авторизация пользователя
        ApiMethods.login_user(email, password)

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, password, new_username)
        assert update_response.status_code == 200 and update_response.json()['user']['name'] == new_username

    @allure.title("Тест на изменение пароля авторизованного пользователя")
    def test_change_user_password(self, user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        password = user_data['password']
        username = user_data['username']
        token = user_data['token']
        new_password = Helper.generate_password()

        # Авторизация пользователя
        ApiMethods.login_user(email, password)

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, new_password, username)
        assert update_response.status_code == 200 and update_response.json()['success'] == True


    @allure.title("Тест на изменение email неавторизованного пользователя")
    def test_change_unauthorized_user_email(self, user_data):
        # Данные для регистрации пользователя
        password = user_data['password']
        username = user_data['username']
        new_email = Helper.generate_email()
        token = user_data['token']

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_email(token, new_email, password, username)
        assert update_response.status_code == 200 and update_response.json()['user']['email'] == new_email

    @allure.title("Тест на изменение имени неавторизованного пользователя")
    def test_change_unauthorized_user_name(self, user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        password = user_data['password']
        token = user_data['token']
        new_username = Helper.generate_email()

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, password, new_username)
        assert update_response.status_code == 200 and update_response.json()['user']['name'] == new_username

    @allure.title("Тест на изменение пароля неавторизованного пользователя")
    def test_change_unauthorized_user_password(self, user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        username = user_data['username']
        token = user_data['token']
        new_password = Helper.generate_password()

        # Обновление данных пользователя
        update_response = ApiMethods.change_user_name(token, email, new_password, username)
        assert update_response.status_code == 200 and update_response.json()['success'] == True


    @allure.title("Тест на изменение email пользователя без поля авторизации")
    def test_change_unauthorized_user_email_without_authorization(self, user_data):
        # Данные для регистрации пользователя
        email = user_data['email']
        password = user_data['password']
        username = user_data['username']
        new_email = Helper.generate_email()

        # Регистрация пользователя
        ApiMethods.register_user(email, password, username)

        # Обновление данных пользователя
        token=''
        update_response = ApiMethods.change_user_email(token,new_email, password, username)
        assert update_response.status_code == 401 and update_response.json()["message"]== "You should be authorised"



