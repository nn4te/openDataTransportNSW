import datetime 
import pandas as pd

beginningDate = datetime.date(2020,1,1)
d = beginningDate
print(d)

while d <= datetime.date(2020,1,1): #date.today():
	print(d)
	yearFolder = d.strftime('%Y') + "-" + d.strftime('%m')
	file = open(yearFolder + "/Opal_Patronage" + d.strftime('%Y%m%d') + ".txt", "r")
	dataFrame = pd.read_csv(file, sep = '|')
	
	d += datetime.timedelta(days=1)

print(dataFrame)


#df = pd.read_csv()