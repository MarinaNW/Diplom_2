from api_methods import ApiMethods
from data import Data
import allure



@allure.title("Тесты на получение заказа пользователя")
class TestReceiveOrder:

    @allure.title("Тест на получение заказа авторизованного пользователя")
    def test_receive_order_of_authorized_user(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        token = response.json().get('accessToken')

        ingredients_data = ApiMethods.get_ingredients()

        ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data'][:2]]
        ApiMethods.create_order(ingredient_ids,token)

        receive_response = ApiMethods.receive_order(token)
        assert receive_response['success'] == True

    @allure.title("Тест на получение заказа неавторизованного пользователя")
    def test_receive_order_of_unauthorized_user(self):
        response = ApiMethods.login_user(Data.email, Data.password)
        login_token = response.json().get('accessToken')

        ingredients_data = ApiMethods.get_ingredients()

        ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data'][:2]]
        ApiMethods.create_order(ingredient_ids,login_token)

        order_token=''
        receive_response = ApiMethods.receive_order(order_token)
        assert receive_response['message'] == "You should be authorised"

