"""class for testing the order_shipping method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time
import os


@freeze_time("2023-03-08")
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.delivery_file = os.path.join(os.path.dirname(__file__),"..\..\JsonFiles\FR2Json") + \
                     "store_shipping.json"

    def test_ecv_1(self):
        "prueba correcta que guarda la informacion de envio"
        my_manager = OrderManager()
        input_file = my_manager.path + "input_files.json"
        my_manager.send_product(input_file)

    def test_ecv_2(self):
        "duplica el nodo comandos"
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba2.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_2_1(self):
        "no hay nada en el json"
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba2.1.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_3(self):
        "Repite { al inicio"
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba3.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_4(self):
        # repite " delante de OrderID
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba4.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_5(self):
        # cambia el OrderID por hola
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba5.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("Invalid JSON format", prueba.exception.message)

    def test_ecv_6(self):
        # repite : detras de OrderID
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba6.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_7(self):
        # repite el " antes del SHA256
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba7.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_8(self):
        #pongo un Order id no aceptado por la regex
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba8.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON has not the expected structure", prueba.exception.message)

    def test_ecv_9(self):
        # elimino el , despues del SHA256
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba9.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_10(self):
        #cambio ContactEmail por hola
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba10.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("Invalid JSON format", prueba.exception.message)

    def test_ecv_11(self):
        #en lugar de un diccionario pongo una lista
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba11.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", prueba.exception.message)

    def test_ecv_12(self):
        #nombre de correo no cumple con la regex establecida
        my_manager = OrderManager()
        input_file = my_manager.path + "FR2Json/prueba12.json"
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.send_product(input_file)
        self.assertEqual("JSON has not the expected structure", prueba.exception.message)