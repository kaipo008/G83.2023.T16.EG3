"""class for testing the order_shipping method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


@freeze_time("2023-03-08")
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        "hace un setup"
        store = "/Users/crown/Desktop/UNI/2ºCurso/G83.2023.T16.EG3/src/JsonFiles/" + \
                     "delivery_files.json"
    def test_ecv_1(self):
        "prueba de que la sintasis este bien"
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("8e290b2ebc51e1634f124c9f1151f88c", my_manager_id)
