import json 
import requests
from pprint import pprint
from time import sleep
from datetime import datetime
from time_rn import right_time # imports the time function

class Get_Github_Info:
    def __init__(self):
        self.username = "kubernetes" # sets the username
        self.repository = "kubernetes" #set the repo name
        
    
    def wait_function(self):
        time_now = right_time() #gets the time
        sleep(302) #waits 5 mins
        return time_now#returns the time before 5 mins

    def get_updated_file(self, username, repository,time):    
        new_dates = []
        response = requests.get('https://api.github.com/repos/{}/{}/events'.format(username,repository)).json() # gets all of the commits within the last 5 mins
        start_date = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
        
        for i in range(len(response)):
            
            file_ = response[i]
            if file_['type'] == "PushEvent":
                file_times = file_['created_at']
                current_date = datetime.strptime(file_times[:-1], "%Y-%m-%dT%H:%M:%S")
                
                if current_date > start_date:
                    new_dates.append(i)
            else:
                pass
        print(new_dates)
        for i in range(len(new_dates)):
            try: 
                commit_info = requests.get(response[i]['payload']['commits'][0]['url']).json()       
            
                for i in range(len(new_dates)):   
                    print(username)
                    json_commit = {'commit':[{'username':username,
                    'repo_name':repository,
                    'date':commit_info['commit']['author']['date'],
                    'email':commit_info['commit']['author']['name'],
                    'name':commit_info['commit']['author']['name'],
                    'comment_count':commit_info['commit']['comment_count'],
                    'message':commit_info['commit']['message'],
                    'files_changed':len(commit_info['files'])}]}
                    print(json_commit)
            except KeyError:
                pass
repos = {
     1: {
        "user_name" : "freeCodeCamp",
        "repo_name" : "freeCodeCamp"
    },
     2: {
        "user_name" : "996icu",
        "repo_name" : "996.ICU"
    },
     3: {
        "user_name" : "Sandkelp",
        "repo_name" : "create"
    },
     4: {
        "user_name" : "EbookFoundation",
        "repo_name" : "free-programming-books"
    },
     5: {
        "user_name" : "googleapis",
        "repo_name" : "googleapis"
    },
     6: {
        "user_name" : "huggingface",
        "repo_name" : "nlp"
    },
     7: {
        "user_name" : "kautukkundan",
        "repo_name" : "Awesome-Profile-README-templates"
    },
     8: {
        "user_name" : "Hack-with-Github",
        "repo_name" : "Awesome-Hacking"
    },
     9: {
        "user_name" : "papers-we-love",
        "repo_name" : "papers-we-love"
    },
     0: {
        "user_name" : "EcloudControl",
        "repo_name" : "util-jun2020"
    }
}
g = Get_Github_Info()# starts the class
while 1==1:
    for i in range(len(repos)):
        g.get_updated_file(repos[i]['user_name'],repos[i]['repo_name'],g.wait_function()) #every 5 mins gets updates

