import boto3
from datetime import datetime
from time import sleep

s3Client = boto3.client('s3')
lambdaClient = boto3.client('lambda')

bucketName = "inputbucket546"
lambdaName = "cse546"

lastCheckedTime = datetime.date(2023, 1, 1)
newTimes = []

while True:
	s3MetaData = s3Client.list_objects_v2(Bucket=bucketName)
	s3ObjectsList = s3MetaData['Contents']
    
	for object in s3ObjectsList:
		if object['LastModified'] > lastCheckedTime:
			newTimes.append(object['LastModified'])
			payload = {'key': object['Key']}
			lambdaClient.invoke(FunctionName=lambdaName, InvocationType='Event', Payload=payload)
	
	lastCheckedTime = max(newTimes)
	newTimes = []
	sleep(5)