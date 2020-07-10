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
        
    def first_print(self):
        time_now = right_time() #gets the time 
        print("Public events for the repository {} in {} since {}: \n".format(self.repository,self.username,time_now) )# title
        response = requests.get('https://api.github.com/repos/{}/{}/commits?since={}Z'.format(self.username,self.repository,time_now)).json() #gets the commits from the start of the code
        pprint(response) #prints them
    
    def wait_function(self):
        time_now = right_time() #gets the time
        sleep(300) #waits 5 mins
        return time_now #returns the time before 5 mins

    def get_updated_file(self, time):
        new_file = requests.get('https://api.github.com/repos/{}/{}/commits?since={}Z'.format(self.username,self.repository,time)).json()# gets all of the commits within the last 5 mins
        pprint(new_file) #prints out the commits within the last 5 mins
        #return len(new_file), new_file
        
    

    
    
        
    


g = Get_Github_Info()# starts the class
g.first_print() #calls the first list of commits
while 1==1:
    g.get_updated_file(g.wait_function()) #every 5 mins the commits are printed
