import pandas as pd
import pandas_gbq
import os
import sys
import random 
from google.oauth2 import service_account
from time import sleep
from datetime import datetime, timedelta, date

def get_data():

    MIN = int(os.environ.get('FETCH_MIN', "10000"))
    MAX = int(os.environ.get('FETCH_MAX', "100000"))
    BATCH_SLEEP = int(os.environ.get('BATCH_SLEEP', "10"))
    BATCH_SIZE = int(os.environ.get('BATCH_SIZE', "1000"))

    path_to_credentials = os.environ.get('CRED_JSON_PATH', 'Quickstart-c97bee3c4606.json')
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


    query = 'SELECT * FROM `bigquery-public-data.wikipedia.pageviews_2020`  WHERE DATE(datehour) = "{}" AND TIME(datehour) = "{}:00:00" AND wiki= "en" LIMIT {}'.format(date_now,current_hour,number_of_responses)
    print("query:", query)

    wiki = pandas_gbq.read_gbq(query)
    
    df = wiki.drop(["datehour"], axis=1)
    print("len(df):", len(df))
    
    start_of_batch=0    
    #response returner
    while start_of_batch < number_of_responses:
 
        end_of_batch = start_of_batch + BATCH_SIZE

        if end_of_batch > number_of_responses:
            end_of_batch = number_of_responses

        print("batch start: {} to {} ({})".format(start_of_batch, end_of_batch, BATCH_SIZE))

        for i in range(end_of_batch - start_of_batch):
        
            try :

                df_record = toStr(df.index[i + start_of_batch])

                df_wiki = toStr(df['wiki'][i + start_of_batch])
                
                df_title = toStr(df['title'][i + start_of_batch])
                
                df_views = toStr(df['views'][i + start_of_batch])

                print('record: ' + df_record +  ', wiki: ' + df_wiki +  ', title: ' + df_title +  ', views: ' + df_views)

            except:

                print("Unexpected error:", sys.exc_info()[0])

        print("batch end: {} to {}".format(start_of_batch, end_of_batch))

        start_of_batch = start_of_batch + BATCH_SIZE

        BATCH_SIZE = random.randrange(0,10000)

        print("batch sleep: {}".format(BATCH_SLEEP))
        sleep(BATCH_SLEEP)
        
def toStr(value):
    try:

        return str(value).encode(encoding='ascii', errors='ignore').decode('ascii')

    except UnicodeEncodeError:

        return "n/a"  

    
print(sys.getdefaultencoding())

while True:

    get_data()
    start_time = 60 - int(datetime.now().minute)
    print("outer loop sleep: {}".format(start_time))
    sleep(start_time * 60)
