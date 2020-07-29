import pandas as pd

import pandas_gbq

from google.oauth2 import service_account

import random 

from time import sleep

from datetime import datetime

def get_data():

    path_to_credentials = 'Quickstart-c97bee3c4606.json'

    credentials1 = service_account.Credentials.from_service_account_file( path_to_credentials )#gets the credentials
    
    # Gets the info from google
    pandas_gbq.context.credentials = credentials1

    pandas_gbq.context.project = "quickstart-1584643705530"

    try: 

        from collections import abc as collections_abc

    except ImportError: 

        import collections as collections_abc

    MIN = 100000

    MAX = 1000000

    number_of_responses = random.randrange(MIN, MAX)# sets a random value of vlues to retrieve


    current_hour = int(datetime.now().hour) - 1

    if current_hour < 0:

        current_hour = 23


    date = datetime.now().strftime("%Y-%m-%d")

    query = 'SELECT * FROM `bigquery-public-data.wikipedia.pageviews_2020`  WHERE DATE(datehour) = "{}" AND TIME(datehour) = "{}:00:00" LIMIT {}'.format(date,current_hour,number_of_responses)

    wiki = pandas_gbq.read_gbq(query)
    
    df = wiki.drop(["datehour"],axis=1)
    
    start_of_batch=0

    #response returner
    while x < number_of_responses:

        BATCH_SIZE = random.randrange(0,10000)

        end_of_batch = BATCH_SIZE 
        
        print(df[start_of_batch:end_of_batch])

        start_of_batch = start_of_batch + BATCH_SIZE

        BATCH_SLEEP = 10

        sleep(BATCH_SLEEP)
    

while True:

    date_hour_min = datetime.now().strftime('%Y-%m-%d %H:%M:00')

    date_and_hour = datetime.now().strftime('%Y-%m-%d %H:42:00')
    
    if date_hour_min == date_and_hour:
       get_data()
