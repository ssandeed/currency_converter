import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => To be filled by student

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    # => To be filled by stude
    """
    if len(args) != 3:
        raise SystemExit("[ERROR] You need to provide 3 arguments in the following order:\n <date> <currency1> <currency2>")
    else:
        return True

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

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
    format = '%Y-%m-%d'
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise SystemExit("Provided date is invalid")

check_date('2022-07-28')