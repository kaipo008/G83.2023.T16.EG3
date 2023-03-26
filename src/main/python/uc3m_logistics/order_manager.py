"""Module """
import json
import re
from .order_request import OrderRequest
from .order_shipping import OrderShipping
from .order_management_exception import OrderManagementException

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        #RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        #OR FALSE IN OTHER CASE
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
        if len(ean13_code) < 20 or len(ean13_code) >= 100:
            raise OrderManagementException("Invalid address length")
        return True

    @staticmethod
    def validate_phone_number(phone_number):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        if not isinstance(phone_number, str):
            raise OrderManagementException("Invalid phone_number")
        if len(phone_number) != 12:
            raise OrderManagementException("Invalid phone_number")
        if not phone_number[0] == "+":
            raise OrderManagementException("Invalid phone_number")
        for i in range(len(phone_number) - 1):
            if not phone_number[i + 1].isdigit():
                raise OrderManagementException("Invalid phone_number")
        return True

    @staticmethod
    def validate_zip_code(zip_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        if not isinstance(zip_code, str):
            raise OrderManagementException("Invalid zip_code")
        if len(zip_code) != 5:
            raise OrderManagementException("Invalid zip_code")
        if not zip_code.isdigit():
            raise OrderManagementException("Invalid zip_code")
        if int(zip_code[0:2]) < 1:
            raise OrderManagementException("Invalid zip_code")
        if int(zip_code[0:2]) > 52:
            raise OrderManagementException("Invalid zip_code")
        return True

    @staticmethod
    def register_order(product_id, order_type, address, phone_number, zip_code):
        """Devuelve el id del producto"""
        OrderManager.validate_ean13(product_id)
        OrderManager.validate_order_type(order_type)
        OrderManager.validate_address(address)
        OrderManager.validate_phone_number(phone_number)
        OrderManager.validate_zip_code(zip_code)
        my_order = OrderRequest(product_id, order_type, address, phone_number, zip_code)

        file_store = "/Users/crown/Desktop/UNI/2ºCurso/G83.2023.T16.EG3/src/JsonFiles/" + "store_patient.json"
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        exist = OrderManager.does_it_exist("OrderID", my_order.order_id, data_list)
        new_data = {
            "OrderID": my_order.order_id,
            "ProductID": my_order.product_id,
            "OrderType": my_order.order_type,
            "Address": my_order.delivery_address,
            "Phone number": my_order.phone_number,
            "ZipCode": my_order.zip_code
        }
        if not exist:
            data_list.append(new_data)
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        return my_order.order_id

    @staticmethod
    def validate_input_file(input_file):
        if input_file[-5:] != ".json":
            raise OrderManagementException("Input file not JSON")
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        if list(input_list.keys()) != ['OrderID', 'ContactEmail']:
            raise OrderManagementException("Invalid JSON format")
        regex = r'^{\s*"OrderID"\s*:\s*"[0-9a-f]{32}",\s*"ContactEmail"\s*:\s*"[a-zA-Z0-9._%+-' \
                r']+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"\s*}$'
        coincidencia = re.match(regex, str(input_list).replace("'", '"'))
        if coincidencia is None:
            raise OrderManagementException("JSON has not the expected structure")
        return input_list

    @staticmethod
    def store_shipping(tracking_code, delivery_day):
        file_store = "/Users/crown/Desktop/UNI/2ºCurso/G83.2023.T16.EG3/src/JsonFiles/" + "store_shipping.json"
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        new_data = {
            "TrackingCode": tracking_code,
            "DeliveryDate": delivery_day
            }
        data_list.append(new_data)
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex


    @staticmethod
    def send_product(input_file):
        input_list = OrderManager.validate_input_file(input_file)
        file_store = "/Users/crown/Desktop/UNI/2ºCurso/G83.2023.T16.EG3/src/JsonFiles/" + "store_patient.json"
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["OrderID"] == input_list["OrderID"]:
                found = True
                order = i
                break
        if not found:
            raise OrderManagementException("Order not in stored orders")
        ship = OrderShipping(order["ProductID"], order["OrderID"], input_list["ContactEmail"], order["OrderType"])
        OrderManager.store_shipping(ship.tracking_code, ship.delivery_day)
        return ship.tracking_code

    @staticmethod
    def does_it_exist(primary_key, primary_key_value, input_list: list):
        exist = False
        for i in input_list:
            if i[primary_key] == primary_key_value:
                exist = True
                break
        return exist
