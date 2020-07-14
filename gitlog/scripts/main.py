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
        sleep(300) #waits 5 mins
        return time_now #returns the time before 5 mins

    def get_updated_file(self, time):
        response = requests.get('https://api.github.com/repos/{}/{}/commits?since={}Z'.format(self.username,self.repository,time)).json()# gets all of the commits within the last 5 mins
        if len(response) == 0:
            pass
        else:
            for i in range(len(response)):
                new_file = response[i]
                json_commit = {'commit':[{'date':new_file['commit']['author']['date'],'email':new_file['commit']['author']['name'],'name':new_file['commit']['author']['name'],'comment_count':new_file['commit']['comment_count'],'message':new_file['commit']['message']}]}
                print(json_commit)

g = Get_Github_Info()# starts the class
while 1==1:
    g.get_updated_file(g.wait_function()) #every 5 mins gets updates
