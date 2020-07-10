from datetime import datetime
from pytz import timezone
from pytz import all_timezones
def right_time():
    fmt = "%Y-%m-%d %H:%M:%S"
    now_utc = datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone('Etc/GMT0'))
    return now_pacific.strftime(fmt)
print(right_time())