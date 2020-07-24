import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
import random 
from time import sleep
def get_data():
    credentials1 = service_account.Credentials.from_service_account_file('Quickstart-c97bee3c4606.json')#gets the credentials 
    pandas_gbq.context.credentials = credentials1 
    pandas_gbq.context.project = "quickstart-1584643705530"
    try: 
        from collections import abc as collections_abc
    except ImportError: 
        import collections as collections_abc
    number_of_responses = random.randrange(100,100000) # sets a random value of vlues to retrieve
    wiki = pandas_gbq.read_gbq('SELECT * FROM `bigquery-public-data.wikipedia.pageviews_2020`  WHERE DATE(datehour) = "2020-07-23" LIMIT {}'.format(number_of_responses))
    df = wiki.drop(["datehour"],axis=1) # delets the datehour column 
    print(df)


while True:
    sleep_time = random.randrange(1,60) # set a random number of minutes between calls
    sleep(sleep_time * 60) #turns the minutes into seconds
    get_data()
