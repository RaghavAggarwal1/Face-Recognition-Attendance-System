# Face-Recognition-Attendance-System

## Summary:
The Hybrid Cloud Classroom Assistant is an innovative solution designed to bridge resources from both Amazon Web Services (AWS) and OpenStack. It seamlessly integrates the vast capabilities of AWS with the flexibility and openness of OpenStack, offering an application that scales on demand and operates cost-effectively.

## Technologies:

* Amazon Web Services (AWS): Leveraging its compute, storage, and various other services to handle video processing and data storage.

* OpenStack: Deployed as an Infrastructure-as-a-Service (IaaS) platform. OpenStack not only manages compute, storage, and network resources but also integrates with AWS services, acting as the hub for our cloud app.


## Features:

1. OpenStack Deployment:
* Customized setup on either physical computers or VMs.
* Utilizes Devstack for swift and hassle-free installation.
* Integrated dashboard for comprehensive resource management.

2. Smart Classroom Assistant:
* Allows educators to upload classroom videos.
* Utilizes AWS's robust Lambda functions for video processing.
* Face recognition capabilities to identify students in videos.
* Fetches and presents academic information of recognized students from a DynamoDB database.

3. Lambda Function Capabilities:
* ffmpeg integration for efficient video frame extraction.
* Python's face_recognition library for accurate face detection and identification.
* Seamless integration with DynamoDB to fetch academic data.

## Implementation Details:
![Description Image](/image.png)

## Resources & References:

* Devstack GitHub
* Face Recognition Library
* Project Resources on GitHub