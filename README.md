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

