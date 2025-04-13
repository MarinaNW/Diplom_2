from api_methods import ApiMethods
from data import Data
from helpers import Helper
import pytest
import allure


@allure.title("Тесты на создание заказа")
class TestCreateOrder:

    @allure.title("Тест на создание заказа с авторизацией")
    def test_create_order_of_authorized_user(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        token = response.json().get('accessToken')

        ingredients_data = ApiMethods.get_ingredients()

        ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data'][:2]]
        create_response = ApiMethods.create_order(ingredient_ids, token)

        assert create_response.json()['success'] == True
        print(f"Созданный заказ: {create_response.json()}")


    @allure.title("Тест на создание заказа без авторизации")
    def test_create_order_of_unauthorized_user(self):
        token = ""
        ingredients_data = ApiMethods.get_ingredients()

        ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data'][:2]]
        create_response = ApiMethods.create_order(ingredient_ids,token)

        assert create_response.json()['success'] == True


    @allure.title("Тест на создание заказа с ингредиентом")
    def test_create_order_with_ingredients(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        token = response.json().get('accessToken')

        ingredients_data = ApiMethods.get_ingredients()

        ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data'][:2]]
        create_response = ApiMethods.create_order(ingredient_ids,token)

        assert create_response.json()['success'] == True


    @allure.title("Тест на создание заказа без ингредиентов")
    def test_create_order_with_ingredients(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        token = response.json().get('accessToken')

        ingredient_ids = ""
        create_response = ApiMethods.create_order(ingredient_ids,token)

        assert create_response.json()['message'] == "Ingredient ids must be provided"


    @allure.title("Тест на создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_ingredients(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        token = response.json().get('accessToken')

        create_response = ApiMethods.create_order(Data.ingredient_ids, token)

        assert create_response.status_code == 500


