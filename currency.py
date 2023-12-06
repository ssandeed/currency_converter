import sys
import frankfurter
from frankfurter import Frankfurter


class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """

    def __init__(self, from_currency, to_currency, date):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.amount = 1
        self.frankfurter = Frankfurter()


    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Other-wise the program will exit and display the relevant message provided in the assignment brief

        """
        f_currency = self.from_currency
        t_currency = self.to_currency
        if f_currency not in Frankfurter().get_currencies_list() and t_currency not in Frankfurter().get_currencies_list():
            raise SystemExit(f"{f_currency} and {t_currency} are not a valid currency codes")
        elif f_currency not in Frankfurter().get_currencies_list():
            raise SystemExit(f"{f_currency} is not a valid currency code")
        elif t_currency not in Frankfurter().get_currencies_list():
            raise SystemExit(f"{t_currency} is not a valid currency code")
        else:
            return True


    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal
        places and save it back in the class attribute inverse_rate.
        """
        self.inverse_rate = round(1/self.get_historical_rate(),4)
        return self.inverse_rate

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.
        """
        return round(self.rate,4)

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the
        currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the
        assignment brief
        """
        self.rate_dic = self.frankfurter.get_historical_rate(self.from_currency,self.to_currency, self.date)
        self.rate = self.rate_dic['rates'][self.to_currency]
        self.rate = self.round_rate(self.rate)
        return self.rate
