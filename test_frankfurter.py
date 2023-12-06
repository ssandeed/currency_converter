import unittest
import requests

import frankfurter
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """
    def test_url(self):
        self.assertIsNone(frankfurter.Frankfurter.__init__(self))

class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """
    def test_currency_list(self):
        self.currency_url = requests.get('https://www.frankfurter.app/currencies/')
        self.expected_value1 = list(self.currency_url.json().keys())
        self.assertEqual(Frankfurter().get_currencies_list(),self.expected_value1)

class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    def test_currency_check(self):
        with self.assertRaises(SystemExit):
            Frankfurter().check_currency('INd')
        with self.assertRaises(SystemExit):
            Frankfurter().check_currency('INR')
        with self.assertRaises(SystemExit):
            Frankfurter().check_currency(123)

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    def test_historical_rate(self):
        self.expected_value1 = 79.863
        self.expected_value2 = 0.0125
        self.expected_value3 = 0.0126
        self.assertEqual(round(Frankfurter().get_historical_rate('USD','INR','2022-08-23')['rates']['INR'],4),self.expected_value1)
        self.assertEqual(round(Frankfurter().get_historical_rate('INR','USD','2022-08-23')['rates']['USD'],4),self.expected_value2)
        self.assertEqual(round(Frankfurter().get_historical_rate('INR','USD','2022-08-30')['rates']['USD'],4),self.expected_value3)
        self.assertEqual(round(Frankfurter().get_historical_rate('inr','usd','2022-08-30')['rates']['USD'],4),self.expected_value3)

if __name__ == '__main__':
    unittest.main()