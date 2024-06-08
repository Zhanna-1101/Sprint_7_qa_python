from methods import Methods as method
from data_generator import TestCreatorData as data
from data import TextServerResponse as text
import allure


class TestDeleteCourier:

    @allure.title('Проверка API удаления курьера')
    @allure.description('Удаление курьера при указании валидного id курьера, проверка кода и тела ответа')
    def test_delete_courier_successful(self, login=data.create_login(), password=data.create_password()):
        method.create_courier(login, password)
        response = method.get_id_and_delete_courier(login, password)
        assert response.status_code == 200 and response.text == text.SUCCESSFUL_REMOVAL

    @allure.title('Проверка API удаления курьера')
    @allure.description('Удаление курьера при указании несуществующего id курьера, проверка кода и тела ответа')
    def test_delete_courier_by_nonexistent_id_fail(self, id=data.id_courier()):
        response = method.delete_courier(id)
        assert response.status_code == 404 and response.json()['message'] == text.NOT_SUCH_COURIER

    @allure.title('Проверка API удаления курьера')
    @allure.description('Удаление курьера при неуказании id курьера,  проверка кода и тела ответа')
    # Данный тест падает, так как возвращается ответ, не соответствующий требованиям.
    def test_delete_courier_without_id_fail(self, id=None):
        response = method.delete_courier(id)
        assert response.status_code == 400 and response.json()['message'] == text.NOT_FOUND_COUTIER
