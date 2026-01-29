import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'  

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomdate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomdate

print("Random date =", getRandomDate("1/1/2000", "12/12/2026"))
