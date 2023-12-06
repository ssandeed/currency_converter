import datetime
import json

from api import call_get

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.
    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """

    def __init__(self):
        base_url = 'https://www.frankfurter.app/'
        self.base_url = base_url
        currencies_url = call_get('https://www.frankfurter.app/currencies/')
        self.currencies_url = currencies_url
        historical_url = call_get('https://www.frankfurter.app/')
        self.historical_url = historical_url

    def get_currencies_list(self):
        list_json = self.currencies_url.json()
        list1 = list(list_json.keys())
        return list1
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

    def check_currency(self, currency):
        currency_list = self.get_currencies_list()
        if str(currency).upper() not in currency_list:
            raise SystemExit(f"{str(currency)} is not a valid currency code")
        else:
            raise SystemExit(f"{str(currency)} is a valid currency code")

        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        from_date = str(from_date)
        to_currency = str(to_currency).upper()
        url = self.base_url + str(from_date) + "?" + "from=" + str(from_currency).upper() + "&" + "to=" + str(to_currency)
        return call_get(url).json()
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """


