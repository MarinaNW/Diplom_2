import pytest

from api_methods import ApiMethods
from helpers import Helper


# Фикстура уровня функции (каждый тест получает отдельную регистрацию и удаление)
@pytest.fixture(scope="function")
def user_data():
   # Генерация данных пользователя
     email = Helper.generate_email()
     password = Helper.generate_password()
     username = Helper.generate_name()

     # Регистрация пользователя
     response = ApiMethods.register_user(email, password, username)
     token = response.json().get('accessToken')

     yield {
         'email': email,
         'password': password,
         'username': username,
         'token': token
     }

     ApiMethods.delete_user(token)

# @pytest.fixture(scope="function")
# def cleanup_user():
#     def remove_user(email, password):
#         # Вход в аккаунт пользователя для получения токена
#         login_response = ApiMethods.login_user(email, password)
#         token = login_response.json().get('accessToken')
#
#         # Удаление пользователя
#         ApiMethods.delete_user(token)
#
#     return remove_user








