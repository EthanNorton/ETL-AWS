from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

# Initialize contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Define AWS Glue job parameters
# In this example, this is to track certain KPIs from the data quality, after data quality has been performed and we select the data we want
job.init('FocusRoutesFeatureEngineering', args)  # Adjust JOB_NAME as per your convention

# Connecting to the data quality validated dataset
input_data = glueContext.create_dynamic_frame.from_catalog(database="Improvements", table_name="FocusRoutes")

# Convert DynamicFrame to DataFrame for Spark SQL operations
df = input_data.toDF()

# Apply transformations using Spark DataFrame API
# This should count the occurences or routes that 
output_data = df.groupBy("column_name").count()

# Example: Calculate average count per group as an optimization KPI
avg_count = df.groupBy("column_name").agg({"count": "avg"})

# From here, I can also combine with the pattern recognition to prepare variables for visualization, etc, which can then be transmitted into
# dashboards, etc. 

# Print or use these KPIs for further analysis or visualization
print(f"Average count per group: {avg_count}")

# Write data back to Glue catalog or other targets as needed
glueContext.write_dynamic_frame.from_options(frame=output_data,
                                             connection_type="s3",
                                             connection_options={"path": "s3://output_path"},
                                             format="csv")

# End AWS Glue job
job.commit()
