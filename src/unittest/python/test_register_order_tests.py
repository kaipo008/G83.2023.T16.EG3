"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager
from freezegun import freeze_time


class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    @freeze_time("2023-03-08")
    def test_ecv_1( self ):
        """dummy test"""
        my_manager = OrderManager()
        my_manager_id = my_manager.register_order\
            ("8421691423220", "REGULAR", "C/LISBOA, 4,MADRID, SPAIN", "+34123456789", "28005")
        self.assertEqual("b305885f8a3c9586e11a919330a1f06d", my_manager_id)
        #comprobar el fichero


if __name__ == '__main__':
    unittest.main()
