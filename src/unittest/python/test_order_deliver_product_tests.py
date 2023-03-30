"""class for testing the deliver_product method"""
import unittest
import json
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.delivery_file = "/Users/crown/Desktop/UNI/2ºCurso/G83.2023.T16.EG3/src/JsonFiles/" + \
                     "delivery_files.json"

    @freeze_time("2023-03-15")
    def test_sp_01(self):
        """Todos los parámetros correctos"""
        my_manager = OrderManager()
        delivery = my_manager.deliver_product("e8274da0545e47f3668477fea61f66ef0301f0b6a549c463bbdfff484901d6f1")
        with open(self.delivery_file, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        OrderManager.does_it_exist("TrackingCode", "e8274da0545e47f3668477fea61f66ef0301f0b6a549c463bbdfff484901d6f1", data_list)
