import math as m
import requests
import xmltodict
import json
import random

import threading
import time

import os





rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", 
         "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", 
         "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", 
         "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]





# URL of the XML data




# WRITE TO FILE WITH DATA

def pullCurrInfo(base):

    # make directory

    



    date = "2011-05-04"
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    print(url)
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)
    


    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict, indent=4)

    # Print the JSON data
    print(json_data)

    # Optionally, write the JSON data to a file
    with open(f"currInfo//{date}_exchange_rates_{base}.json", "w") as json_file:
        json_file.write(json_data)

    
    with open(f"currInfo//{date}_exchange_rates_{base}.xml", "w") as json_file:
        json_file.write(response.text)


def task(name):
    print(f"Thread {name}: starting")
    pullCurrInfo(name)
    print(f"Thread {name}: finishing")

   


if __name__ == "__main__":
    
    # thread these all the base rates
    # for r in ratesForBase:
    #     pullCurrInfo(r)

    base = random.choice(ratesForBase)

    print(base)

    pullCurrInfo(base)


    threads = []

    for r in ratesForBase:
        thread = threading.Thread(target=task, args=(base,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads completed")


