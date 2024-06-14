## Project: Package Tracking and Exception Handling Pipeline

### Description
This project implements an ETL (Extract, Transform, Load) pipeline to track package status and handle delivery exceptions. 
The pipeline extracts data from various sources, including package scanning systems and customer feedback, transforms the data to categorize exceptions, performs data quality checks, and loads it into a centralized Amazon Redshift database. 
Real-time dashboards are created using AWS Quicksight for monitoring and managing exceptions.
This is similar to other experiences I have, just learning new tools and names for Amazon Stack.

### Skills Utilized
- **AWS Glue:** Used for data extraction, transformation, loading, and data quality checks.
- **Amazon Redshift:** Centralized data warehousing solution.
- **Amazon S3:** Scalable storage for raw and processed data.
- **AWS Quicksight:** Data visualization and dashboard creation.
- **Python:** Scripting for data transformation and automation.
- **Data Integration:** Combining data from various sources.
- **ETL:** Extract, Transform, Load processes.
- **Data Quality:** Perform data quality checks to ensure data is prepared for deeper analysis.
- **Feature Engineering:** Prepare feature modification and checks based on requests.
- **Performance Tuning:** Optimize data processes for better performance.
- **Pattern Recognition:** Programmatically identify patterns in data for insights.

### Table of Contents
1. [Project Structure](#project-structure)
2. [Setup Instructions](#setup-instructions)
3. [Data Extraction](#data-extraction)
4. [Data Transformation](#data-transformation)
5. [Data Quality Checks](#data-quality-checks)
6. [Feature Engineering](#feature-engineering)
7. [Performance Tuning](#performance-tuning)
8. [Pattern Recognition](#pattern-recognition)
9. [Data Loading](#data-loading)
10. [Dashboard Creation](#dashboard-creation)
11. [Monitoring and Exception Management](#monitoring-and-exception-management)
12. [Solutions and Process Optimization](#solutions-and-process-optimization)
13. [Requirements](#requirements)

### Project Structure
![image](https://github.com/EthanNorton/ETL-AWS/assets/86625413/e64820d5-983d-47a9-b077-6dde181664eb)

### File Structure
![image](https://github.com/EthanNorton/ETL-AWS/assets/86625413/1978a0a6-d3de-49c7-91cd-f029578e2d53)

### Data Extraction

Script: extract_data.py

- Extract data from package scanning systems and customer feedback sources.
- Save raw data to data/raw/.

### Data Transformation 

Script: transform_data.py

- Clean and normalize the extracted data.
- Categorize delivery exceptions.
- Save transformed data to data/processed/.

### Data Quality Checks

Script: data_quality_checks.py

- Define data quality rules using AWS Glue.
- Perform data quality checks to ensure data integrity.
- Save quality-checked data to data/quality_checked/.

### Feature Engineering

Script: feature_engineering.py

- Develop new features based on data requirements.
- Modify and check features to enhance data usability.
- Save engineered features to data/engineered/.

### Performance Tuning

Script: performance_tuning.py

- Optimize data extraction, transformation, and loading processes.
- Implement best practices for performance improvements.
- Save optimized configurations and results to data/optimized/.

### Pattern Recognition

Script: pattern_recognition.py

- Use algorithms to identify patterns in data.
- Apply machine learning techniques for deeper insights.
- Save pattern recognition results to data/patterns/.

### Data Loading 

Script: load_data.py

- Load the quality-checked and feature-engineered data into Amazon Redshift.
- Utilize AWS Glue for orchestration.

### Dashboard Creation 

- Create real-time dashboards using AWS Quicksight.
- Import the package_tracking_dashboard.quicksight file into AWS Quicksight.
- Configure the dashboard to use the data from Redshift.

### Monitoring and Exception Management

- Monitor the dashboards for real-time insights.
- Use Quicksight alerts to manage and address delivery exceptions.
- Create new variables or views based of ETL to monitor exceptions.
- Use Quicksight alerts to manage and address delivery exceptions.

### Solutions and Process Optimization

Document: solutions_and_optimization.md

- Detailed solutions and optimizations implemented during the project.
- Documentation of the processes and methodologies used.
- Recommendations for future improvements.

### Growth Areas and Rooms for Improvements

Document: growth-areas.md


### Requirements 

pip install -r requirements.txt
