"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


@freeze_time("2023-03-08")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_ecv_1(self):
        """dummy test"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order\
             ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("8e290b2ebc51e1634f124c9f1151f88c", my_manager_id)

    def test_ecv_2(self):
        """Product ID not a number"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("Invalid EAN13 code string", prueba.exception.message)

    def test_ecv_3(self):
        """Product ID not check sum"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423225", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("Invalid EAN13 code string", prueba.exception.message)

    def test_ecv_4(self):
        """Order_type wrong"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order \
                ("8421691423220", "PRE", "C/LISBOA,4, MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("Invalid order_type", prueba.exception.message)

    def test_ecv_5(self):
        """19 characters for address, cota inferior invalida"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order \
                ("8421691423220", "PREMIUM", "C/LIS,4, MADR, SPAI", "+34123456789", "28005")
        self.assertEqual("Invalid address length", prueba.exception.message)

    def test_ecv_6(self):
        """20 characters for address, cota inferior valida"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "PREMIUM", "C/LIS,4, MADR, SPAIN", "+34123456789", "28005")
        self.assertEqual("9a6397e11aed67e554fcf245af4eb43c", my_manager_id)

    def test_ecv_7(self):
        """99 characters for address, cota superior valida"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "PREMIUM", "C/LISBOA LA MEJOR CIUDAD DEL MUND0,12345678999, "
            "MADRID DEMASIADA CONTAMINACION, SPAIN PERO SIN LA S", "+34123456789", "28005")
        self.assertEqual("3eb1a4fb8c37ffc300fae92c0714e48c", my_manager_id)

    def test_ecv_8(self):
        """100 characters for address, cota superior invalida"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order \
                ("8421691423220", "PREMIUM", "C/LISBOA LA MEJOR CIUDAD DEL MUND0,123456789999, "
                "MADRID DEMASIADA CONTAMINACION, SPAIN PERO SIN LA S", "+34123456789", "28005")
        self.assertEqual("Invalid address length", prueba.exception.message)

    def test_ecv_9(self):
        """numero telefono bien"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("8e290b2ebc51e1634f124c9f1151f88c", my_manager_id)

    def test_ecv_10(self):
        """tiene letras"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+1a123456789", "28005")
        self.assertEqual("Invalid phone_number", prueba.exception.message)

    def test_ecv_23(self):
        """tiene 11 cifras"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+1123456789", "28005")
        self.assertEqual("Invalid phone_number", prueba.exception.message)

    def test_ecv_11(self):
        """tiene 13 cifras"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+111123456789", "28005")
        self.assertEqual("Invalid phone_number", prueba.exception.message)

    def test_ecv_12(self):
        """tiene letras"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "12312a456789", "28005")
        self.assertEqual("Invalid phone_number", prueba.exception.message)

    def test_ecv_13(self):
        """codigo postal bien"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("8e290b2ebc51e1634f124c9f1151f88c", my_manager_id)

    def test_ecv_14(self):
        """6 digitos"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "280105")
        self.assertEqual("Invalid zip_code", prueba.exception.message)

    def test_ecv_15(self):
        """4 digitos"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "2805")
        self.assertEqual("Invalid zip_code", prueba.exception.message)

    def test_ecv_16(self):
        """tiene letras"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "280a5")
        self.assertEqual("Invalid zip_code", prueba.exception.message)

    def test_ecv_17(self):
        """first 2 digit less than 01"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "00005")
        self.assertEqual("Invalid zip_code", prueba.exception.message)

    def test_ecv_18(self):
        """first 2 digit more than 52"""
        my_manager = OrderManager()
        with self.assertRaises(OrderManagementException) as prueba:
            my_manager.register_order\
                ("8421691423220", "PREMIUM", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "99005")
        self.assertEqual("Invalid zip_code", prueba.exception.message)

    def test_ecv_19(self):
        """justo 01"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "01005")
        self.assertEqual("c6f1b7087cba778077d8011d698c2ab0", my_manager_id)

    def test_ecv_20(self):
        """justo 52"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order \
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "52005")
        self.assertEqual("7bd1f4edccea9bb9fd17e5ef1098e150", my_manager_id)

    def test_ecv_correct(self):
        """dummy test"""
        my_manager = OrderManager()
        input_file = my_manager.path + "input_files.json"
        ship = my_manager.send_product(input_file)

    @freeze_time("2023-03-15")
    def test_entrega(self):
        my_manager = OrderManager()
        delivery = my_manager.deliver_product\
            ("e8274da0545e47f3668477fea61f66ef0301f0b6a549c463bbdfff484901d6f1")


if __name__ == '__main__':
    unittest.main()
