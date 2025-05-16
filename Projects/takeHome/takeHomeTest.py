import math as m
import requests
import xmltodict
import json
import xml.etree.ElementTree as ET
import random
from datetime import datetime, timedelta
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
    try:
        root =  ET.fromstring(respose)
    except ET.ParseError as e:
        logger.error(f"Error parsing XML string: {e}")
        return []
    # create empty list for news items
    newsitems = []

    # iterate news items
    
    logger.info('parssing info ')
    # empty news dictionary
    news = {}
    
    

    for item_element in root.findall('item'):
        item_details = {}
        # Iterate through all child elements of the current <item>
        for child_element in item_element:
            item_details[child_element.tag] = child_element.text
        if item_details: # Ensure we only add non-empty item data
            newsitems.append(item_details)


    print(newsitems)
    return newsitems
  


def savetoCSV(newsitems):

    # specifying the fields for csv file
    fields = ['title', 'baseCurrency', 'targetCurrency', 'exchangeRate', 'inverseRate' ]

    # writing to csv file
    if os.path.exists(f"./allDB.csv"):
            with open(f"./allDB.csv", 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = fields,extrasaction='ignore' )
                writer.writerows(newsitems)
    else:
        with open(f"./allDB.csv", 'w') as csvfile:

            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames = fields,extrasaction='ignore' )

            # writing headers (field names)
            writer.writeheader()

            # writing data rows
            writer.writerows(newsitems)


def pullCurrInfo(base,date):

    # make directory

    directories_path = f"currInfo/{base}"
    os.makedirs(directories_path, exist_ok=True)



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

    
    with open(f"currInfo//{base}//{date}_exchange_rates_{base}.xml", "w", encoding="utf-8") as json_file:
        json_file.write(response.text)


def task(name,date):
    threadsPool.acquire()
    try:
        print(f"Thread {name}: starting")
        logger.info(f"{name} Start")
        pullCurrInfo(name,date)
        print(f"Thread {name}: finishing")
        logger.info(f"{name} Done")
    finally:
        threadsPool.release()




def increment_date_string(startdate, enddate):
    try:
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    try:
        end_date_object = datetime.strptime(enddate, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
    
    if date_object > end_date_object:
        return "Start date cannot be after end date."
    
    dates = []
    current_date = date_object
    while current_date <= end_date_object:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    
    return dates

    
   
if __name__ == "__main__":
    

    max_threads = 100
    threadsPool = threading.Semaphore(max_threads)

    os.remove("log//kingsLogs.log")
    logger = logging.getLogger("file_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("log//kingsLogs.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)

    try:
        os.remove("allDb.csv")
    except:
        logger.warning("no DB found")

 
        
    
        

    logger.warning("Starting Threads - GATHERING SCROLLS :)")


    threads = []

    date = "2011-05-04"
    r = random.choice(rates)
    for x in increment_date_string(date, "2025-05-04"):
        thread = threading.Thread(target=task, args=(r,x,))
        threads.append(thread)
        thread.start()


    # for r in ratesForBase:
    #     thread = threading.Thread(target=task, args=(r,))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    print("All threads completed")
    logger.info("Program Finished - ALL THE SCROLLS ARE BACK")


