import unittest
import temperature_converter

class Test_Temperature(unittest.TestCase):
    def test_convert_from_celsius_to_farenheit(self):
        temp_celcius = 5
        self.assertEqual(41,temperature_converter.celsius_to_fahrenheit(temp_celcius))

    def test_convert_from_fahrenheit_to_celsius(self):
        temp_fahr = 32
        self.assertEqual(0,temperature_converter.fahrenheit_to_celsius(temp_fahr))

    def test_determine_freezing_temperature(self):
        temp_c = -5
        self.assertTrue(temperature_converter.is_freezing(temp_c))

    def test_determine_not_freezing_temperature(self):
        temp_c = 5
        self.assertFalse(temperature_converter.is_freezing(temp_c))
        

