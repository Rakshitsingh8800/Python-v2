import datetime

for month in range(1, 13):
    print(datetime.date(1, month, 1).strftime("%B"))