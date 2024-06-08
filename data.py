class Urls:

    MAIN_URL = 'http://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{MAIN_URL}/api/v1/courier'
    LOGIN_COURIER = f'{MAIN_URL}/api/v1/courier/login'
    DELETE_COURIER = f'{MAIN_URL}//api/v1/courier'
    CREATE_ORDER = f'{MAIN_URL}/api/v1/orders'
    GET_LIST_ORDERS = f'{MAIN_URL}/api/v1/orders'


class TextServerResponse:

    SUCCESSFUL_CREATION = '{"ok":true}'
    NOT_ENOUGH_DATA = 'Недостаточно данных для создания учетной записи'
    LOGIN_IS_BUSY = 'Этот логин уже используется. Попробуйте другой.'
    SUCCESSFUL_LOGIN = 'id'
    NOT_ENOUGH_DATA_TO_LOGIN = 'Недостаточно данных для входа'
    NOT_FOUND_DATA = 'Учетная запись не найдена'
    SUCCESSFUL_ORDER = 'track'
    SUCCESSFUL_GET_LIST_ORDERS = 'orders'
    SUCCESSFUL_REMOVAL = '{"ok":true}'
    NOT_FOUND_COUTIER = 'Not Found.'
    NOT_SUCH_COURIER = 'Курьера с таким id нет.'
