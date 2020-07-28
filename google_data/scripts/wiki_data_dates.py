import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
import random 
from time import sleep
from datetime import datetime
def get_data():
    credentials1 = service_account.Credentials.from_service_account_file('C:\\Users\\ssubh\\OneDrive\\Desktop\\cto\\github_prj\\Quickstart-c97bee3c4606.json')#gets the credentials
    #C:\\Users\\ssubh\\OneDrive\\Desktop\\cto\\github_prj\\Quickstart-c97bee3c4606.json
    
    # Gets the info from google
    pandas_gbq.context.credentials = credentials1
    pandas_gbq.context.project = "quickstart-1584643705530"
    try: 
        from collections import abc as collections_abc
    except ImportError: 
        import collections as collections_abc
    number_of_responses = random.randrange(100,100000)# sets a random value of vlues to retrieve
    x = str(datetime.now())
    hour = int(x[11:13]) - 1 # sets the hour back
    date = x[:10]
    wiki = pandas_gbq.read_gbq('SELECT * FROM `bigquery-public-data.wikipedia.pageviews_2020`  WHERE DATE(datehour) = "{}" AND TIME(datehour) = "{}:00:00" LIMIT {}'.format(date,hour,number_of_responses))
    df = wiki.drop(["datehour"],axis=1)
    x=0
    while x < number_of_responses:
        batch_size = random.randrange(0,10000)
        print(df[x:(batch_size + x)])
        x = x + batch_size
        sleep(10)
    


    
    



while True:
    real_time = str(datetime.now())
    date_hour_min = real_time[:19]
    date_and_hour = real_time[:13]
    if date_hour_min == '{}:48:00'.format(date_and_hour):
       get_data()
