# Can also go more in depth in this one, but this in combination with domain knowledge will help select which KPIs to focus on
# based on problematic areas, etc to focus on what to select for QuickSight

import pandas as pd

# Load data from Glue table into Pandas DataFrame
df = spark.read.format("glueparquet").load("database_name.table_name").toPandas()

# Statistical summary
summary_stats = df.describe()

# Correlation matrix
correlation_matrix = df.corr()
