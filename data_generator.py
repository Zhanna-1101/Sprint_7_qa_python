from faker import Faker
from datetime import date
from random import randint


class TestCreatorData:

    # Метод создания логина курьера
    @staticmethod
    def create_login():
        login = Faker().user_name()
        return login

    # Метод создания пароля курьера
    @staticmethod
    def create_password():
        password = Faker().password()
        return password

    # Метод создания имени курьера, пользователя
    @staticmethod
    def create_firstname():
        firstName = Faker(locale='ru_RU').first_name()
        return firstName

    # Метод создания фамилии пользователя
    @staticmethod
    def create_lastName():
        lastName = Faker(locale="ru_RU").last_name()
        return lastName

    # Метод создания адреса пользователя
    @staticmethod
    def create_address():
        address = Faker(locale="ru_RU").street_address()
        return address

    # Метод выбора станции метро
    @staticmethod
    def choose_metroStation():
        metroStation = randint(1, 215)
        return metroStation

    # Метод создания номера телефона пользователя
    @staticmethod
    def create_phone():
        phone = Faker(locale="ru_RU").phone_number()
        return phone

    # Метод выбора срока аренды самоката
    @staticmethod
    def set_rentTime():
        rentTime = randint(1, 5)
        return rentTime

    # Метод выбора даты доставки самоката
    @staticmethod
    def set_deliveryDate():
        deliveryDate = str(date.today())
        return deliveryDate

    # Метод создания комментария
    @staticmethod
    def create_comment():
        comment = Faker().text(max_nb_chars=25)
        return comment

    # Метод выбора цвета
    @staticmethod
    def choose_color():
        color = [[''], ['BLACK'], ['GREY'], ['BLACK', 'GREY']]
        return color

    # Метод создания рандомного id курьера
    @staticmethod
    def id_courier():
        id_courier = randint(100000, 1000000)
        return id_courier
