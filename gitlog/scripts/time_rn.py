from datetime import datetime
from pytz import timezone # imports timezones
def right_time():
    fmt = "%Y-%m-%d %H:%M:%S" # formats the date and time
    now_utc = datetime.now(timezone('UTC')) #gets the current time
    now_pacific = now_utc.astimezone(timezone('Etc/GMT0')) # sets the time 4 hours ahead for github to return what was just commited
    return now_pacific.strftime(fmt) $ #sets the time for the github api to use 
w
