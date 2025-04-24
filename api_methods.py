import allure
import requests
from curl import CURL

class ApiMethods:

    @staticmethod
    def register_user(email, password, username):
        with allure.step('Регистрация пользователя'):
            return requests.post(CURL.register_user, json={"email": email,"password": password,"name": username})

    @staticmethod
    def get_user_data(access_token):
        with allure.step('Получение данных пользователя'):
           headers = {'Authorization': f'Bearer+{access_token}'}
           return requests.get(CURL.data_user, headers=headers)

    @staticmethod
    def change_user_email(access_token, new_email, password, username):
        with allure.step('Изменение email пользователя'):
            headers = {'Authorization': f'Bearer+{access_token}'}
            return requests.patch(CURL.data_user, json={"email": new_email,"password": password,"name": username}, headers=headers)

    @staticmethod
    def change_user_name(access_token, email, password, new_username):
        with allure.step('Изменение имени пользователя'):
            headers = {'Authorization': f'Bearer+{access_token}'}
            return requests.patch(CURL.data_user, json={"email": email,"password": password,"name": new_username}, headers=headers)

    @staticmethod
    def change_user_password(access_token, email, new_password, username):
        with allure.step('Изменение пароля пользователя'):
            headers = {'Authorization': f'Bearer+{access_token}'}
            return requests.patch(CURL.data_user, json={"email": email,"password": new_password,"name": username}, headers=headers)

    @staticmethod
    def delete_user(access_token):
        with allure.step("Получение данных об ингредиентах"):
            headers = {'Authorization': f'Bearer+{access_token}'}
            return requests.delete(CURL.delete_user, headers=headers)


    @staticmethod
    def login_user(email, password):
        with allure.step('Авторизация пользователя'):
            return requests.post(CURL.login_user, json={"email": email, "password": password})


    @staticmethod
    def get_ingredients():
        with allure.step("Получение данных об ингредиентах"):
            response = requests.get(CURL.ingredients)
            return response.json()

    @staticmethod
    def receive_order(access_token):
        with allure.step("Получение данных о заказе пользователя"):
            headers = {'Authorization': f'Bearer{access_token}'}
            response = requests.get(CURL.create_order, headers=headers)
            return response
            #return response.json()

    @staticmethod
    def create_order(ingredients,access_token):
        with allure.step('Создание заказа'):
            headers = {'Authorization': f'Bearer{access_token}'}
            return requests.post(CURL.create_order, json={"ingredients": ingredients}, headers=headers)



