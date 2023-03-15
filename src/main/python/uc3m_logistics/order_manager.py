"""Module """
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        #CE_NV_2
        if not ean13_code.isdigit():
            raise OrderManagementException("Invalid EAN13 code string")
        #CE_NV_3
        if not isinstance(ean13_code, str):
            raise OrderManagementException("Invalid EAN13 code string")
        if len(ean13_code) != 13:
            raise OrderManagementException("Invalid EAN13 code string")
        index = 0
        result = 0
        while index < 12:
            if index % 2 == 0:
                result += int(ean13_code[index])
            else:
                result += 3 * int(ean13_code[index])
            index += 1
        aux = result
        while aux % 10 != 0:
            aux += 1
        aux -= result
        if aux != int(ean13_code[index]):
            raise OrderManagementException("Invalid EAN13 code string")
        return True

    @staticmethod
    def validate_order_type(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        if ean13_code.upper() != "REGULAR" and ean13_code.upper() != "PREMIUM":
            raise OrderManagementException("Invalid order_type")
        return True

    @staticmethod
    def validate_address(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        a = len(ean13_code)
        if len(ean13_code) < 20 or len(ean13_code) >= 100:
            raise OrderManagementException("Invalid address length")
        return True

    @staticmethod
    def validate_phone_number(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        return True

    @staticmethod
    def validate_zip_code(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        return True

    @staticmethod
    def register_order (product_id, order_type, address, phone_number, zip_code):
        """Devuelve el id del producto"""
        OrderManager.validate_ean13(product_id)
        OrderManager.validate_order_type(order_type)
        OrderManager.validate_address(address)
        my_order = OrderRequest(product_id, order_type, address, phone_number, zip_code)
        return my_order.order_id
