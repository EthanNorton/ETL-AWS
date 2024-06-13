## Project: Package Tracking and Exception Handling Pipeline

### Description
This project implements an ETL (Extract, Transform, Load) pipeline to track package status and handle delivery exceptions. 
The pipeline extracts data from various sources, including package scanning systems and customer feedback, transforms the data to categorize exceptions, and loads it into a centralized Amazon Redshift database. 
Real-time dashboards are created using AWS Quicksight for monitoring and managing exceptions.
This is similar to other experiences I have, just learning new tools and names for Amazon Stack.

### Skills Utilized
- **AWS Glue:** Used for data extraction, transformation, and loading.
- **Amazon Redshift:** Centralized data warehousing solution.
- **Amazon S3:** Scalable storage for raw and processed data.
- **AWS Quicksight:** Data visualization and dashboard creation.
- **Python:** Scripting for data transformation and automation.
- **Data Integration:** Combining data from various sources.
- **ETL:** Extract, Transform, Load processes.

### Table of Contents
1. [Project Structure](#project-structure)
2. [Setup Instructions](#setup-instructions)
3. [Data Extraction](#data-extraction)
4. [Data Transformation](#data-transformation)
5. [Data Loading](#data-loading)
6. [Dashboard Creation](#dashboard-creation)
7. [Monitoring and Exception Management](#monitoring-and-exception-management)
8. [Requirements](#requirements)


### Project Structure
![image](https://github.com/EthanNorton/ETL-AWS/assets/86625413/64c0be55-9792-4cc4-898a-d92c377f6818)



### Data Extraction

Script: extract_data.py

- Extract data from package scanning systems and customer feedback sources.
- Save raw data to data/raw/.

### Data Transformation 

Script: transform_data.py

- Clean and normalize the extracted data.
- Categorize delivery exceptions.
- Save transformed data to data/processed/

### Data Loading 

Script: load_data.py

- Load the transformed data into Amazon Redshift.
- Utilize AWS Glue for orchestration.

### Dashboard Creation 

- Create real-time dashboards using AWS Quicksight.
- Import the package_tracking_dashboard.quicksight file into AWS Quicksight.
- Configure the dashboard to use the data from Redshift.
- **Monitoring and Exception Management**
- Monitor the dashboards for real-time insights.
- Use Quicksight alerts to manage and address delivery exceptions.



### Requirements 
pip install -r requirements.txt
