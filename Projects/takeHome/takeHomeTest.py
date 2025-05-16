import math as m
import requests
import xmltodict
import json
import xml.etree.ElementTree as ET
import random

import threading
import time
import csv
import os

import logging





# https://www.geeksforgeeks.org/xml-parsing-python/
# really good info on parsing xml and saving to csv 

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", 
         "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", 
         "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", 
         "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]





# URL of the XML data




# WRITE TO FILE WITH DATA

def fetchDataFromXML(respose):
    # create element tree object
    tree = ET.parse(respose)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel'):
        logger.info()
        # empty news dictionary
        news = {}
        logger.info
        print(item)
        # iterate child elements of item
        # for child in item:
        #     news[child.tag] = child.text
         
                

        # # append news dictionary to news items list
        # newsitems.append(news)
    
    # return news items list
    return newsitems


def savetoCSV(newsitems):

    # specifying the fields for csv file
    fields = ['title', 'baseCurrency', 'targetCurrency', 'exchangeRate', 'inverseRate' ]

    # writing to csv file

    with open(f"./allDB.csv", 'w') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)


def pullCurrInfo(base):

    # make directory

    directories_path = f"currInfo/{base}"
    os.makedirs(directories_path, exist_ok=True)



    date = "2011-05-04"
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    print(url)
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)
    savetoCSV(fetchDataFromXML(response.text))
    


    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict, indent=4)

    # Print the JSON data
    print(json_data) 

    # Optionally, write the JSON data to a file
    with open(f"currInfo//{base}//{date}_exchange_rates_{base}.json", "w") as json_file:
        json_file.write(json_data)

    
    with open(f"currInfo//{base}//{date}_exchange_rates_{base}.xml", "w") as json_file:
        json_file.write(response.text)


def task(name):
    print(f"Thread {name}: starting")
    logger.info(f"{name} Start")
    pullCurrInfo(name)
    print(f"Thread {name}: finishing")
    logger.info(f"{name} Done")



if __name__ == "__main__":
    
    # thread these all the base rates
    # for r in ratesForBase:
    #     pullCurrInfo(r)

    os.remove("log//kingsLogs.log")
    logger = logging.getLogger("file_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("log//kingsLogs.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)



    logger.warning("Starting Threads - GATHERING SCROLLS :)")
    threads = []


    r = random.choice(rates)
    thread = threading.Thread(target=task, args=(r,))
    threads.append(thread)
    thread.start()

    # for r in ratesForBase:
    #     thread = threading.Thread(target=task, args=(r,))
    #     threads.append(thread)
    #     thread.start()

    for thread in threads:
        thread.join()

    print("All threads completed")
    logger.info("Program Finished - ALL THE SCROLLS ARE BACK")


