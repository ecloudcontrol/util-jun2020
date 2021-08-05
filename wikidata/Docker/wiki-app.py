import pandas as pd
import pandas_gbq
import os
import sys
import random 
from google.oauth2 import service_account
from time import sleep
from datetime import datetime, timedelta, date
from flask import Flask, Response 
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge, generate_latest

wikiApp1 = Flask(__name__)

metrics = {}

metrics['c'] = Counter('number_of_responses', 'The total number of responses recorded')

metrics['g'] = Gauge('last_num_of_responses', 'Last amount of responses')

metrics['v'] = Counter('number_of_views', 'The total number of views for the wikiData')

metrics['b'] = Gauge('last_batch_size', 'Last batch size for wikiData')


def toStr(value):
    try:
        return str(value)
    except UnicodeEncodeError:
        return "n/a"
        
@wikiApp1.route('/')
def get_data():
    while True:

        MIN = 100000
        MAX = 1000000
        BATCH_SLEEP = 30   # change back to 10
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

        metrics['c'].inc(number_of_responses) # sends the metric of number of responses
        metrics['g'].set(number_of_responses) # sets the amount for the gauge metric

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

                    metrics['v'].inc(6)

                except:

                    print("Unexpected error:", sys.exc_info()[0])

            print("batch end: {} to {}".format(start_of_batch, end_of_batch))

            start_of_batch = start_of_batch + BATCH_SIZE

            BATCH_SIZE = random.randrange(0,10000)

            print("batch sleep: {}".format(BATCH_SLEEP))
            sleep(BATCH_SLEEP)
        #eturn(toStr(wiki))

        #start_time = 60 - int(datetime.now().minute)
        #sleep(start_time * 60)

        return('done')
        
    
        
@wikiApp1.route('/metrics')
def prometheus_metrics():
    res = []
    for k, v in metrics.items():
        res.append(generate_latest(v))
    return Response(res, mimetype="text/plain") 
    
  
    
    
print(sys.getdefaultencoding())

