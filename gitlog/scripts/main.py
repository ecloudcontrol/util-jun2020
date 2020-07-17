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
        self.ref = "refs/heads/20200702/j2y"
    
    def wait_function(self):
        time_now = right_time() #gets the time
        sleep(300) #waits 5 mins
        return time_now#returns the time before 5 mins

    def get_updated_file(self, username, repository,time):
        response = requests.get('https://api.github.com/repos/{}/{}/commits?since={}Z'.format(username,repository,time)).json()# gets all of the commits within the last 5 mins
        num_files = requests.get('https://api.github.com/repos/{}/{}/commits/master'.format(username,repository)).json()
        if len(response) == 0:
            pass
        else:
            for i in range(len(response)):
                print(username)
                new_file = response[i]
                json_commit = {'commit':[{'username':username,
                'repo_name':repository,
                'date':new_file['commit']['author']['date'],
                'email':new_file['commit']['author']['name'],
                'name':new_file['commit']['author']['name'],
                'comment_count':new_file['commit']['comment_count'],
                'message':new_file['commit']['message'],
                'files_changed':len(num_files['files'])}]}
                print(json_commit)
        
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
        "user_name" : "vuejs",
        "repo_name" : "vue"
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
        "user_name" : "TowhidKashem",
        "repo_name" : "snapchat-clone"
    }
}
g = Get_Github_Info()# starts the class
while 1==1:
    for i in range(len(repos)):
        g.get_updated_file(repos[i]['user_name'],repos[i]['repo_name'],g.wait_function()) #every 5 mins gets updates

