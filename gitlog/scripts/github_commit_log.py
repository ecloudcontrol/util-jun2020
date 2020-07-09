import json 
import requests
from pprint import pprint
from time import sleep

class Get_Github_Info:
    def __init__(self):
        self.username = ""#username here
        self.repository = ""#reponame here
        print("Public events for the repository {} in {}: \n".format(self.repository,self.username))
        response = requests.get('https://api.github.com/repos/{}/{}/commits'.format(self.username,self.repository)).json()
        pprint(response)
    def get_updated_file(self):
        new_file = requests.get('https://api.github.com/repos/{}/{}/commits'.format(self.username,self.repository)).json()
        return len(new_file), new_file
        
    

    
    
        
    def compare_files(self, file1, file2):
        sleep(5)
        if file1 == file2:
            return True
        else:
            return False




g = Get_Github_Info()
while 1==1:
    status1, content1 = g.get_updated_file()
    sleep(5) 
    status2, content2 = g.get_updated_file()
    status = g.compare_files(status1, status2)
    if status == True:
        pass
    elif status == False:
        pprint(content2[status1:status2])





