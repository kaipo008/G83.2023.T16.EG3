"""Module """
from .order_request import OrderRequest


class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        return True

    @staticmethod
    def register_order (product_id, order_type, address, phone_number, zip_code):
        """Devuelve el id del producto"""
        my_order = OrderRequest(product_id, order_type, address, phone_number, zip_code)
        return my_order.order_id
