import pandas as pd
import pandas_gbq
import os
import sys
import random 
from google.oauth2 import service_account
from time import sleep
from datetime import datetime, timedelta, date
from flask import Flask 

wikiApp = Flask(__name__)

def toStr(value):
    try:
        return str(value)
    except UnicodeEncodeError:
        return "n/a"
        
@wikiApp.route('/')
def get_data():
    while True:

        MIN = 100000
        MAX = 1000000
        BATCH_SLEEP = 10
        BATCH_SIZE = 10000

        path_to_credentials = 'quickstart-1584643705530-af0712b55af8.json'
        #os.environ.get('CRED_JSON_PATH', 'quickstart-1584643705530-38de96f4fb94.json')
        print("Using credentials from ", path_to_credentials) 

        # Gets the info from google
        pandas_gbq.context.credentials = service_account.Credentials.from_service_account_file( path_to_credentials ) #gets the credentials
        
        pandas_gbq.context.project = os.environ.get('PROJECT_NAME', "quickstart-1584643705530")
        print("Project:", pandas_gbq.context.project)

        try: 

            from collections import abc as collections_abc

        except ImportError: 

            import collections as collections_abc

        number_of_responses = random.randrange(MIN, MAX) # sets a random value of vlues to retrieve
        print("number_of_responses:", number_of_responses)

        current_hour = int(datetime.now().hour) - 4
        date_now = datetime.now().strftime("%Y-%m-%d")

        if current_hour < 0:

            current_hour = 24 + current_hour
            date_now = date.today() - timedelta(days=1)

        query = 'SELECT * FROM `bigquery-public-data.wikipedia.pageviews_2021`  WHERE DATE(datehour) = "{}" AND TIME(datehour) = "{}:00:00" AND wiki= "en" LIMIT {}'.format(date_now,current_hour,number_of_responses)

        print("query:", query)

        wiki = pandas_gbq.read_gbq(query)
        
        return(toStr(wiki))

        start_time = 60 - int(datetime.now().minute)
        sleep(start_time * 60)
        
  
    
    
print(sys.getdefaultencoding())
