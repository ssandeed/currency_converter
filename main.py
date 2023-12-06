import datetime
import sys
import checks
import currency
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    """
    Pseudo-code
    ----------
    Extract the input arguments
    Remove the first argument (name of Python script)
    Check there are 3 items in the remaining list of arguments (using your defined check_arguments() function)
    Check the validity of the input date (using your defined check_date() function)
    Instantiate an object from your defined CurrencyConverter class with the verified 2 currency codes and date
    Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
    Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
    """
    arg = sys.argv
    args = arg[1:]
    checks.check_arguments(args)
    checks.check_date(args[0])
    if currency.CurrencyConverter(args[1].upper(),args[2].upper(),args[0]).check_currencies():
        obj1 = currency.CurrencyConverter(args[1].upper(),args[2].upper(),args[0])
        rate = obj1.get_historical_rate()
        inverse_rate = obj1.reverse_rate()
        print(f"The conversion rate on {args[0]} from {args[1].upper()} to {args[2].upper()} was {rate}. The inverse rate was {inverse_rate}")