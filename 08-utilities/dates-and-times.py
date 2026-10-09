# Python Dates and Times

import datetime

date = datetime.date(2005, 6, 18)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

formatted_now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030, 1, 1, 12, 1, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print('Date has Passed')
else:
    print('Date is Coming')
