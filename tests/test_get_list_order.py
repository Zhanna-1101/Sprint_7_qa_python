from data import TextServerResponse as text
from methods import Methods as method
import allure


class TestGetListOrders:

    @allure.title('Проверка API получения списка заказов')
    @allure.description('Получение списка заказов, проверка кода и тела ответа (возвращение списка)')
    def test_getting_list_order_successful(self):
        response = method.get_list_order()
        assert response.status_code == 200
        assert text.SUCCESSFUL_GET_LIST_ORDERS in response.text
        assert type(response.json()['orders']) == list
