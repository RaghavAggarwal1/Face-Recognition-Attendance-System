import boto3
from datetime import datetime
from time import sleep
import csv

s3Client = boto3.client('s3')

bucketName = "outputbucket546"

lastCheckedTime = datetime.date(2023, 1, 1)
newTimes = []

while True:
	s3MetaData = s3Client.list_objects_v2(Bucket=bucketName)
	s3ObjectsList = s3MetaData['Contents']
    
	for object in s3ObjectsList:
		if object['LastModified'] > lastCheckedTime:
			newTimes.append(object['LastModified'])
			s3.download_file(bucketName, object['Key'], '/./'+object['Key'])
			
			with open('key_name.csv', newline='') as csvfile:
				fileReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
				for row in fileReader:
					print(', '.join(row))
	
	lastCheckedTime = max(newTimes)
	newTimes = []
	sleep(5)