import pytest
from methods import Methods as method
from data_generator import TestCreatorData as data
from data import TextServerResponse as text
import allure


class TestLoginCourier:

    @allure.title('Проверка API авторизации курьера')
    @allure.description('''Авторизация курьера при заполнении всех обязательных полей,
                        проверка кода и тела ответа (успешный запрос возвращает id).''')
    def test_login_courier_successful(self, login=data.create_login, password=data.create_password):
        method.create_courier(login, password)
        response = method.login_courier(login, password)
        assert response.status_code == 200 and text.SUCCESSFUL_LOGIN in response.text
        method.delete_courier(response.json()['id'])

    @allure.title('Проверка API авторизации курьера')
    @allure.description('''Авторизация курьера при указании несуществующих логина и пароля.
                        Проверка кода и тела ответа.''')
    def test_login_nonexistent_courier_fail(self, login=data.create_login, password=data.create_password):
        response = method.login_courier(login, password)
        assert response.status_code == 404 and text.NOT_FOUND_DATA in response.text

    @allure.title('Проверка API авторизации курьера')
    @allure.description('''Авторизация курьера когда одно из обязательных полей не заполнено,
                        проверка кода и тела ответа (успешный запрос возвращает id).''')
    @pytest.mark.parametrize('login, password', (['', data.create_password], [data.create_login, '']))
    def test_login_courier_without_login_fail(self, login, password):
        response = method.login_courier(login, password)
        assert response.status_code == 400 and text.NOT_ENOUGH_DATA_TO_LOGIN in response.text
