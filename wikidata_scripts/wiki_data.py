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
    wiki = pandas_gbq.read_gbq('SELECT * FROM `bigquery-public-data.wikipedia.pageviews_2020`  WHERE DATE(datehour) = "2020-07-22" AND TIME(datehour) = "20:00:00" LIMIT {}'.format(number_of_responses))
    df = wiki.drop(["datehour"],axis=1)
    time = str(datetime.now())

    #makes the dates
    mins = time[14:16]
    secs = time[17:19]
    dates = []
    for x in range(len(df)):
        x = str(datetime.now())
        hour = int(x[11:13]) - 1 # sets the hour back
        date = x[:10]
        if int(mins) < 10 and len(str(mins)) < 2: #if there is less than 2 digits in the mins place it adds a 0 in front
            date_time = (str(date) + ' ' + str(hour) + ':'+ '0' + str(mins)+ ':' + str(secs))
            date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S') #formats the string into a date to be sorted later
            dates.append(date_time_obj) # adds the time obj to the array
            

        else:
            date_time = (str(date) + ' ' + str(hour) + ':'+ str(mins)+ ':' + str(secs)) #turns the date into a string
            date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S') #formats the string into a date to be sorted later
            dates.append(date_time_obj) # adds the time obj to the array

        if (random.randrange(1,10) % 2) == 0: #50% chance that the mins will increase
            mins = int(mins) + random.randrange(0,4)
        secs = int(secs) + random.randrange(0,10) # adds the seconds on to the end

        if int(mins) >= 60: # if the mins are above 60 it will reset to 0 secs
            mins = 0 
        if int(secs) >= 60: #if the secs are above 60 it will reset to 0 secs
            secs = 0
    df['datehour'] = dates
    
    df=df.sort_values(by ='datehour' , ascending=True) # the dataframe is sorted by the date and time
    pd.set_option("display.max_rows", None, "display.max_columns", None) # this shows the full data frame
    df1 = df.reset_index() # deletes the old out of order index
    print(df1.drop(["index"],axis=1))



while True:
    sleep_time = random.randrange(0,60)# set a random number of minutes between calls
    sleep(sleep_time*60) #turns the minutes into seconds
    get_data()
