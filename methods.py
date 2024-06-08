import requests
from data import Urls as url
import json


class Methods:

    # Метод создания курьера с логином, паролем и именем
    @staticmethod
    def create_courier_full_data(login, password, firstName):
        payload = {'login': login, 'password': password, 'firstName': firstName}
        response = requests.post(url.CREATE_COURIER, data=payload)
        return response

    # Метод создания курьера с логином и паролем (только обязателньые поля)
    @staticmethod
    def create_courier(login, password):
        payload = {'login': login, 'password': password}
        response = requests.post(url.CREATE_COURIER, data=payload)
        return response

    # Метод авторизации курьера в системе
    @staticmethod
    def login_courier(login, password):
        payload = {'login': login, 'password': password}
        response = requests.post(url.LOGIN_COURIER, data=payload)
        return response

    # Метод получения id курьера и удаления курьера
    @staticmethod
    def get_id_and_delete_courier(login, password):
        payload = {'login': login, 'password': password}
        resp = requests.post(url.LOGIN_COURIER, data=payload)
        id_courier = resp.json()['id']
        response = requests.delete(f'{url.DELETE_COURIER}/{id_courier}')
        return response

    # Метод удаления курьера
    @staticmethod
    def delete_courier(id):
        id_courier = id
        response = requests.delete(f'{url.DELETE_COURIER}/{id_courier}')
        return response

    # Метод создания заказа
    @staticmethod
    def create_order(firstName, lastName, address, metroStation, phone, 
                     rentTime, deliveryDate, comment, color):
        payload = json.dumps({'firstName': firstName, 'lastName': lastName, 'address': address,
                              'metroStation': metroStation, 'phone': phone, 'rentTime': rentTime,
                              'deliveryDate':  deliveryDate, 'comment': comment, 'color': color})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url.CREATE_ORDER, headers=headers, data=payload)
        return response

    # Метод получения списка заказов по id
    @staticmethod
    def get_list_order():
        response = requests.get(url.GET_LIST_ORDERS)
        return response
