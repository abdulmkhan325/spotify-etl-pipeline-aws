# Spotify ETL using Python and AWS

### Introduction
This project is about building an ETL (Extract, TRansformation, load) pipeline using the Spotify API on AWS. This project focuses on obtaining the artist, album, and song information from the “Global Top 50” playlist on Spotify that is updated weekly.

### Architecture Diagram
![Architecture](https://github.com/abdulmkhan325/spotify-etl-pipeline-aws/blob/main/Architecture.PNG)


### Key Learnings 
-How to extract data from Spotify API 

-Build an automated trigger to run data pipelines (CloudWatch EventBridge trigger) 

-Write extract and transformation jobs (Lambda) and store raw data (S3) 

-Build the correct bucket structure for data storage 

-Automate transformation job (S3 trigger) for new data 

-Build analytics layer for perfomaing SQL queries and business intelligence (Athena)


### Tools used: 
VSCode, Python, AWS services (CloudWatch, Lambda, S3, Glue and Athena)


#### S3 
AWS S3 provides a convenient and scalable solution for storing and accessing large volumes of data. Data is organized into buckets, and each file within S3 is referred to as an object.

#### Lambda
AWS Lambda is a compute service that lets you run code without provisioning or managing servers.

#### CloudWatch (EventBridge)
Monitor and collect metrics from AWS resources. Can be used to monitor log files and set alarms

#### Glue
AWS Glue Crawler was used to automatically scan and analyze the data sources to get their schema and create metadata tables.
AWS Glue Data Catalog was also used as it's a centralized metadata repository that stores and organizes metadata information about various data sources, such as databases, tables, and schemas. 

#### Athena
AWS Athena is a serverless query service provided by Amazon Web Services (AWS). It allows to analyze data stored in Amazon S3 using standard SQL queries without the need to set up and manage infrastructure.

### Prerequisites:

In order to access the Spotify API:

- Create an account on the Spotify Developer Dashboard and register your application to obtain client credentials, including a Client ID and Client Secret.

- Optionally, set up alarms on CloudWatch to receive email notifications for charges exceeding USD 5 and configure Free Tier Usage Alerts.

- Create an S3 bucket with a globally unique name. I chose the us-east-1 region for the bucket. The S3 bucket will have the following folder structure.

/aws-spotify-etl-majid: Main folder in bucket

/raw_data: Raw data is stored here

* to_be_processed: When the data extraction function is invoked, data extracted from the API will be stored here

* processed: When the transformation function is invoked, files in to_process folder will be copied to this folder and the file in to_process will be deleted. We are just moving data from one folder to another.

/transformed_data: These 3 folders will contain the transformed dataset where basic cleaning and transformation have been applied. * /album_data * /artist_data * /song_data

/query-results: This was used as the storage location for AWS Athena's query processing
