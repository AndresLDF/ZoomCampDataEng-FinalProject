# ZoomCamp Data Eng - Final Project

## Introduction

This project is the final project for Data Engineering Zoom Camp. In this project the complete I will share workflow for extracting the information related to the South America fires during the last years and uploading it to buckets and BigQuery for later analysis 

For this project the following technologies are employed:
  - PySpark  
 - Mage AI
 - dbt
 - Google Storate
 - Google BigQuery

The database is extracted from
- [Fire Database from the Brazil Government](http://terrabrasilis.dpi.inpe.br/queimadas/portal/dados-abertos/#da-focos)

The basic flow flow is

 1. The information from the government site is extracted using the PySpark and divide in partitions 
 2. Each partition is uploaded to buckets using the Mage API to trigger a Pipeline
 3. Then a second pipeline is call with the API to upload the information in the bucket files to BigQuary
 4. Then dbt is used to create some working tables
 5. Looker Studio is used to analyze the tables created to condense the information 

## Preparation
Before run this project do the following configuration
**PySpark and MageAI**
1. Go into a local folder and clone this repository with this command `gh repo clone AndresLDF/ZoomCampDataEng-FinalProject`
2. In the main folder add they Json file with the key for BigQuery 
3. Open the file magic-zoomcamp/io_config.yaml
4. In the file search for GOOGLE_SERVICE_ACC_KEY_FILEPATH
5. Replace glossy-grin-413315-49491a38ee63.json with your own json file name

**Google Cloud Configuration**
1. Go to your Google Cloud count account control panel
2.  Go to IAM
3. Go to Service Account
4. Create a Service Account with comple access to Google Storage and BigQuery
5. Download the Json file (this is the one that you use in mage) to the 

**DBT configuration**
1. Go to dbt cloud and create a new project
2. Create a new dbt project
3. Link the project to a git repository
4. Fill the git repository with the files in this repository **[data-engineering-zoomcamp-DBT](https://github.com/AndresLDF/data-engineering-zoomcamp-DBT)**

Other configuration
You have to install in your computer the following:

- Spark
- Python
- Jupyter Notebook
- Docker

## Extracting information and moving it to Google Cloud
Follow the steps below to fulfill the configuration
 1. Start Docker
 2. Open the directory with the repository
 3. Use the command `docker compose build` (do this only the first time)
 4. Use the command `docker compose up`
 5. check that mage is online at http://localhost:6789
 6. Go back to the directory with the repository and star Jupyter Notebook
 7. Open the file "Complete Work Flow.ipynb"
 8. Run all the cells

**running this you will be able to** 
- Download all the files between year 2009 and 2023 for the South America fires
- Create a partitions for each files
- Upload the partitions to Bucket
- Move the information from Buckets to BigQuery
![enter image description here](https://github.com/AndresLDF/ZoomCampDataEng-FinalProject/blob/main/images/1%20-%20Files%20Downloaded.png)
![enter image description here](https://github.com/AndresLDF/ZoomCampDataEng-FinalProject/blob/main/images/2%20-%20Partitions%20Created.png)
![enter image description here](https://github.com/AndresLDF/ZoomCampDataEng-FinalProject/blob/main/images/3%20-%20Partitions%20in%20Buckets.png)
![enter image description here](https://github.com/AndresLDF/ZoomCampDataEng-FinalProject/blob/main/images/4%20-%20Information%20moved%20from%20Buckets%20to%20BigQuery.png)
## Use dbt to modify to create new tables
**Steps to follow**
1. In Dbt cloud open the project with the files from the repository **[data-engineering-zoomcamp-DBT](https://github.com/AndresLDF/data-engineering-zoomcamp-DBT)**
2. Build the file at final_project/models/staging/schema.yml
3. Build the file at final_project/models/staging/staging/stg_staging__all_data.sql
4. Build the file at final_project/models/core/fires_year.sql
5. Build the file at final_project/models/core/year_variation.sql
6. This will create the table fires_year, and year_variation in Bigquery 

![enter image description here](https://github.com/AndresLDF/ZoomCampDataEng-FinalProject/blob/main/images/5%20-%20dbt%20queries.png)
![enter image description here](https://github.com/AndresLDF/ZoomCampDataEng-FinalProject/blob/main/images/6%20-%20New%20Tables%20at%20BigQuery.png)
