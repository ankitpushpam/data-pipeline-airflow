# Twitter Airflow Data Pipeline

This project sets up a data pipeline to extract, transform, and load (ETL) Twitter data into an AWS S3 bucket using Apache Airflow. Follow the steps below to get started.

## Setup Twitter API Access

1. Create a Twitter Developer Account.
2. Create a Twitter App and obtain API keys and access tokens.
3. Copy these keys and tokens for later use.

## Installation and Configuration

### EC2 Instance Setup

1. Launch an AWS EC2 instance (e.g., Ubuntu t3.medium) and configure security groups to allow SSH and HTTP/HTTPS traffic.
2. Download the SSH key pair and keep it secure.
3. Connect to the EC2 instance using SSH.

### Install Required Packages

##### Run the following commands on the EC2 instance:

##### Update package list
sudo apt-get update

##### Install required packages
1. sudo apt install python3-pip 
2. sudo pip install apache-airflow
3. sudo pip install pandas
4. sudo pip install s3fs 
5. sudo pip install tweepy


## Apache Airflow Setup

1. Start the Airflow server on the EC2 instance using `airflow standalone`.
2. Access the Airflow console at `http://<EC2-Public-IPv4-DNS>:8080`.
3. Log in with the admin username and password.

## DAG Configuration

1. Copy the contents of `etl_data_pipeline.py` into a Python file.
2. Create an Airflow DAG by copying the contents of `airflow-dag.py`.
3. Customize the DAG parameters and schedule as needed.
4. Save both files in the Airflow DAG folder on the EC2 instance.

## DAG Configuration

1. Copy the contents of `etl_data_pipeline.py` into a Python file.
2. Create an Airflow DAG by copying the contents of `airflow-dag.py`.
3. Customize the DAG parameters and schedule as needed.
4. Save both files in the Airflow DAG folder on the EC2 instance.
