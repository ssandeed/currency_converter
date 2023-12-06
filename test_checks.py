import unittest
import checks
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    def test_args_length(self):
        self.args = ['2022-07-28', 'USD', 'INR']
        self.assertTrue(checks.check_arguments(self.args))
        with self.assertRaises(SystemExit):
            checks.check_arguments(['USD', 'INR'])
        with self.assertRaises(SystemExit):
            checks.check_arguments(['2022-07-28', 'USD'])
        with self.assertRaises(SystemExit):
            checks.check_arguments(['2022-07-28'])
        with self.assertRaises(SystemExit):
            checks.check_arguments([])

class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    def test_date(self):
        self.assertIsNone(checks.check_date('2022-07-28'))
        with self.assertRaises(SystemExit):
            checks.check_date('2022-07-32')
        with self.assertRaises(SystemExit):
            checks.check_date('2022-07/29')
        with self.assertRaises(SystemExit):
            checks.check_date('2022/07/29')

if __name__ == '__main__':
    unittest.main()