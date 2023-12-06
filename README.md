# Currency Converter in Python

## Description
It is a Python program that will perform currency conversion using data fetched from Frankfurter(https://www.frankfurter.app/), which is an open-source API.

The program will convert currency between 2 currency codes at a specific date. It has also been designed to calculate the inverse conversion rate between these 2 currencies.

***Some major challenges that I faced are:***

  - Writing API code to make connections with API
  - Thinking about the use cases for test cases
  - Understanding the concepts of Object Orientation Programming (OOP)

<Some of the features you hope to implement in the future>
  
***Some features that I hope to implement in the future are:***

  - Implementing UI/UX design to the Currency Converter
  - Line graph of variation of currency rates over a given period
  - Apply Machine Learning Models to classify currencies based on past performance
  - Apply Statistical Models to predict the rate based on past performance

## How to Setup

***Step-by-step description of how to get the development environment set and running:***

  1. Unzip the zip folder
  2. Open PyCharm or other similar development environment
  3. Upload or connect all files into the development environment
  4. Make sure the Python version is as given below
  5. Upload all the packages and their version as given below

***Python packages and version used:***

Python Version: Python 3.8.9 


Package Used        Version
------------------ ---------
certifi            2022.6.15

charset-normalizer 2.1.1

idna               3.3

pip                21.3.1

requests           2.28.1

setuptools         60.2.0

urllib3            1.26.12

wheel              0.37.1


## How to Run the Program

The command terminal will take a specific date in the given format and 2 currency codes as input arguments. Here is the command for running the script:

**`python main.py [date] [currency1] [currency2]`**

The script will return the given outputs for different scenarios:

| Scenario | Example | Output |
| ------------------- | --------------------------------- | ------------------------- |
| Success | `python main.py 2022-08-30 USD AUD` | The conversion rate on 2022-08-30 from USD to AUD was 1.4423. The inverse rate was 0.6933 |
| Missing argument | `python main.py` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2] |
| Missing argument | `python main.py 2022-01-01` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2]|
| Missing argument | `python main.py 2022-01-01 AUD` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2] |
| Too many argument | `python main.py 2022-01-01 AUD EUR GBP` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2] |
| Incorrect currency | `python main.py 2022-01-01 usd AAA` | AAA is not a valid currency code |
| Incorrect currency | `python main.py 2022-01-01 AAA USD` | AAA is not a valid currency code |
| Incorrect currencies | `python main.py 2022-01-01 AAA bbb` | AAA and bbb are not valid currency codes |
| Incorrect date | `python main.py 2022/01/01 AAA USD` | Provided date is invalid |
| Incorrect date | `python main.py 2022-01-41 EUR bbb` | Provided date is invalid |
| API error | | There is an error with Frankfurter API |


## Project Structure
<List all folders and files of this project and provide a quick description for each of them>
***Folder:***
dsp_at1_24622829.zip

***Files within the Zip folder are as follows:***

  - **main.py:** main program used for running your business logic
  - **checks.py:** Python script that will contain the code for checking inputted arguments and the date validity
  - **api.py:** python script that will contain the code for making API calls
  - **frankfurter.py:** Python script that will contain the class used for calling relevant Frankfurter endpoints
  - **currency.py:** python script that will contain the class used for extracting currency conversion rate and calculating the inverse rate
  - **test_checks.py:** Python script for testing code from checks.py
  - **test_frankfurter.py:** python script for testing code from frankfurter.py
  - **test_api.py:** Python script for testing code from api.py
  - **test_currency.py:** Python script for testing code from currency.py
  - **README.md:** a markdown file containing details of the student, a description of the project, a listing of all Python versions and packages and instructions for running your code 

## Citations

*1. Markdown Cheat Sheet | Markdown Guide. (n.d.). Retrieved September 9, 2022, from https://www.markdownguide.org/cheat-sheet/*

*2. Unittest—Unit testing framework—Python 3.10.7 documentation. (n.d.). Retrieved September 9, 2022, from https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs*

*3. rec, yotam. (2021, August 8). Answer to “Python 3.2 input date function.” Stack Overflow. https://stackoverflow.com/a/68703300*

*4. Singh, D. K. (2019, June 2). Answer to “unittest assertionError in python AssertionError: <Response [200]> != 200.” Stack Overflow. https://stackoverflow.com/a/56416987*

*5. Reinhart, J. (2013, May 12). Answer to “Correct way to try/except using Python requests module?” Stack Overflow. https://stackoverflow.com/a/16511493*
