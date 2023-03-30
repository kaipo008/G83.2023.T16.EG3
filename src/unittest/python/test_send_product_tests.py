"""class for testing the order_shipping method"""
import unittest
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException
from freezegun import freeze_time


@freeze_time("2023-03-08")
class MyTestCase(unittest.TestCase):