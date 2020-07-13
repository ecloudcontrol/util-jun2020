import json 
import requests
from pprint import pprint
from time import sleep
from datetime import datetime
from time_rn import right_time # imports the time function

class Get_Github_Info:
    def __init__(self):
        self.username = "Sandkelp" # sets the username
        self.repository = "create" #set the repo name
    
    def wait_function(self):
        time_now = right_time() #gets the time
        sleep(30) #waits 5 mins
        return time_now #returns the time before 5 mins

    def get_updated_file(self, time):
        response = requests.get('https://api.github.com/repos/{}/{}/commits?since={}Z'.format(self.username,self.repository,time)).json()# gets all of the commits within the last 5 mins
        new_file = response[0]
        print('name: ' + str(new_file['commit']['author']['name']))#prints name
        print('comment_count: ' + str(new_file['commit']['comment_count']))# prints comment count
        print('message: ' +str(new_file['commit']['message']))# prints the message
        

g = Get_Github_Info()# starts the class
while 1==1:
    g.get_updated_file(g.wait_function()) #every 5 mins gets updates
