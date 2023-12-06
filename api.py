import requests
import sys

"""
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief
"""

def call_get(url: str) -> requests.models.Response:
    try:
        response = requests.get(url)
    except requests.exceptions.Timeout as t:
    # Maybe set up for a retry, or continue in a retry loop
        raise SystemExit('There is an error with Frankfurter API')
    except requests.exceptions.TooManyRedirects as tmr:
    # Tell the user their URL was bad and try a different one
        raise SystemExit('There is an error with Frankfurter API')
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit('There is an error with Frankfurter API')
    return response


