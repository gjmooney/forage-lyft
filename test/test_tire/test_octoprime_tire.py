import unittest

from tires.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear_array = [1, 1, 1, 0]
        tire = OctoprimeTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear_array = [0.1, 0.2, 0.3, 0.6]
        tire = OctoprimeTire(wear_array)
        self.assertFalse(tire.needs_service())