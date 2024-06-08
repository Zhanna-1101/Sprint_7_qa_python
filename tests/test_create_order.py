import pytest
from methods import Methods as method
from data_generator import TestCreatorData as data
from data import TextServerResponse as text
import allure


class TestCreateOrder:

    @allure.title('Проверка API создания заказа')
    @allure.description('''Проверка успешного создания заказа при указании цвета самоката (черный, серый),
                        выборе двух цветов самоката, неуказании цвета самоката в заказе, проверка кода и тела ответа''')
    @pytest.mark.parametrize('color', [data.choose_color()[0], data.choose_color()[1], data.choose_color()[2], data.choose_color()[3]])
    def test_create_courier_with_full_or_nesessary_data_successful(self, color, firstName=data.create_firstname(), lastName=data.create_lastName(),
                                                                   address=data.create_address(), metroStation=data.choose_metroStation(),
                                                                   phone=data.create_phone(), rentTime=data.set_rentTime(),
                                                                   deliveryDate=data.set_deliveryDate(), comment=data.create_comment()):
        response = method.create_order(firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color)
        assert response.status_code == 201 and text.SUCCESSFUL_ORDER in response.text
