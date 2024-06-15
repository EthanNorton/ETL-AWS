import pandas as pd

# Load data from Glue table into Pandas DataFrame
df = spark.read.format("glueparquet").load("database_name.table_name").toPandas()

# Statistical summary
summary_stats = df.describe()

# Correlation matrix
correlation_matrix = df.corr()
