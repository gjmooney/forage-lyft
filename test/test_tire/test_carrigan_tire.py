import unittest

from tires.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear_array = [0.1, 0.2, 0.3, 0.9]
        tire = CarriganTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear_array = [0.1, 0.2, 0.3, 0.6]
        tire = CarriganTire(wear_array)
        self.assertFalse(tire.needs_service())