import pytest
from methods import Methods as method
from data_generator import TestCreatorData as data
from data import TextServerResponse as text
import allure


class TestCreateCourier:

    @allure.title('Проверка API создания курьера')
    @allure.description('''Создание курьера при заполнении всех полей и только обязательных полей,
                        проверка создания курьера, кода и тело ответа''')
    @pytest.mark.parametrize('login, password, firstName', ([data.create_login, data.create_password, data.create_firstname],
                                                            [data.create_login, data.create_password, '']))
    def test_create_courier_with_full_or_nesessary_data_successful(self, login, password, firstName):
        response = method.create_courier_full_data(login, password, firstName)
        assert response.status_code == 201 and response.text == text.SUCCESSFUL_CREATION
        method.get_id_and_delete_courier(login, password)

    @allure.title('Проверка API создания курьера')
    @allure.description('''Регистрация второго курьера с теми же  данными, логином- невозможна,
                        проверка кода и текста ответа''')
    #  Проверка что регистрация второго курьера с тем же логином- невозможна
    @pytest.mark.parametrize('login, password', ([data.create_login, data.create_password],
                                                 ['SamBridgesPorter', data.create_password]))
    def test_create_second_courier_with_same_data_fail(self, login, password):
        method.create_courier(login, password)
        response = method.create_courier(login, password)
        assert response.status_code == 409 and response.json()['message'] == text.LOGIN_IS_BUSY
        method.get_id_and_delete_courier(login, password)

    @allure.title('Проверка API создания курьера')
    @allure.description('''Регистрация невозможна без заполнения всех обязательных полей,
                        проверка кода и текста ответа''')
    @pytest.mark.parametrize('login, password', ([data.create_login, ''], ['', data.create_password]))
    def test_create_courier_without_necessary_data_fail(self, login, password):
        response = method.create_courier(login, password)
        assert response.status_code == 400 and response.json()['message'] == text.NOT_ENOUGH_DATA
