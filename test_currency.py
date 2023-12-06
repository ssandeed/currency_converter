import unittest
import currency
from currency import CurrencyConverter


class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    def test_instant1(self):
        self.check_value = CurrencyConverter('AUD', 'INR', '2022-08-30')
        self.assertIsInstance(self.check_value, CurrencyConverter)


class TestCurrencyCheck(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """

    def test_currency(self):
        self.check_value = CurrencyConverter('AUD', 'INR', '2022-08-30')
        with self.assertRaises(SystemExit):
            currency.check_value.check_currencies()

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    def test_reverse_check(self):
        self.check_value = CurrencyConverter('AUD', 'INR', '2022-08-30')
        self.assertEqual(self.check_value.reverse_rate(), 0.0181)

class TestRoundRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """

    def test_round(self):
        self.check_value = CurrencyConverter('AUD', 'INR', '2022-08-30')
        self.assertEqual(currency.CurrencyConverter('AUD', 'INR', '2022-08-30').round_rate(0.01813), self.check_value.round_rate(0.01813))


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """

    def test_hist_rate(self):
        self.assertDictEqual(currency.CurrencyConverter('AUD', 'INR', '2022-08-30').get_historical_rate())

if __name__ == '__main__':
    unittest.main()