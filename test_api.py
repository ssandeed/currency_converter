import unittest
import api
from api import call_get

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    def test_api_check(self):
        self.assertEqual(api.call_get('https://www.frankfurter.app/').status_code,200)
        with self.assertRaises(SystemExit):
            api.call_get('www.google.com')

if __name__ == '__main__':
    unittest.main()
