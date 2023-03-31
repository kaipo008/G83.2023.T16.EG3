"""class for testing the deliver_product method"""
import unittest
import json
import os
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time

@freeze_time("2023-03-08")
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.delivery_file = os.path.join(os.path.dirname(__file__),"../../JsonFiles/") + \
                     "delivery_files.json"
        store_patient = os.path.join(os.path.dirname(__file__), "../../JsonFiles/") + \
                        "store_patient.json"
        if os.path.isfile(store_patient):
            os.remove(store_patient)
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "28005")


    @freeze_time("2023-03-15")
    def test_sp_01(self):
        """Todos los parámetros correctos. Fecha regular, + 7 días"""
        my_manager = OrderManager()
        my_manager.deliver_product(
            "82a205608150ed5d5286b94a3c149b1dad6f60dc69d48710e1df925afe623019")
        with open(self.delivery_file, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        exist = OrderManager.does_it_exist("TrackingCode",
                "82a205608150ed5d5286b94a3c149b1dad6f60dc69d48710e1df925afe623019",
                data_list)
        self.assertTrue(exist)

    def test_sp_02(self):
        """Tracking code no registrado en store_shipping"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.deliver_product(
                "e8274da0545e47f3668477fea61f66ef0301f0b6a549c463bbdfff484901d6f2")
        self.assertEqual("Tracking Code not Registered", prueba.exception.message)

    def test_sp_05(self):
        """El tracking code no tiene formato SHA-256"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.deliver_product(
                "e8274da0545e47f3668477fea61f66ef0301f0b6a549c463bbd")
        self.assertEqual("Tracking number is invalid", prueba.exception.message)

    def test_sp_06(self):
        """El tracking code no es procesable (no es str)"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.deliver_product(3)
        self.assertEqual("Tracking code cannot be procesed", prueba.exception.message)

    @freeze_time("2023-03-13")
    def test_sp_06(self):
        """La fecha no entra en el intervalo de entrega. Llega 2 días antes"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.deliver_product(
                "82a205608150ed5d5286b94a3c149b1dad6f60dc69d48710e1df925afe623019")
        self.assertEqual("Fecha no corresponde a la fecha de entrga", prueba.exception.message)

if __name__ == '__main__':
    unittest.main()