import requests
import os
import datetime
from datetime import date

beginningDate = datetime.date(2020,1,11)
d = beginningDate

headers = {
	"referer": "https://opendata.transport.nsw.gov.au/"
}

with requests.Session() as s:
	while d <= date.today():
		print(d)
		yearFolder = d.strftime('%Y') + "-" + d.strftime('%m')
		
		url = "https://tfnsw-prod-opendata-tpa.s3-ap-southeast-2.amazonaws.com/Opal_Patronage/" + yearFolder + "/Opal_Patronage_" + d.strftime('%Y%m%d') + ".txt"

		if not os.path.exists(yearFolder):
			os.makedirs(yearFolder)

		r = s.get(url, headers=headers)
		file = open(yearFolder + "/Opal_Patronage" + d.strftime('%Y%m%d') + ".txt", "wb")
		file.write(r.content)

		d += datetime.timedelta(days=1)


