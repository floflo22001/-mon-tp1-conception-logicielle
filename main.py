from datetime import datetime

current_time = datetime.now()
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted)

import pytz # $ pip install pytz

timezone_paris = pytz.timezone('Europe/Paris')
current_time = datetime.now(timezone_paris)
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted)