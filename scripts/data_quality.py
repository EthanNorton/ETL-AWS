import boto3
import os 
from dotenv import load_dotenv

# Load variables from the .env file into environment variables
load_dotenv()

# Initialize a session using Amazon Glue
session = boto3.Session(region_name='us-west-2')
glue = session.client('glue')

#  I don't have the column name or conditions, but this is an example 
# Other rule set will be more niche, likely from the feature engineering file and be much more in depth
dqdl_rules = """
{
  "rules": [
    {
      "rule-type": "ColumnValues",
      "parameter": {
        "column-name": "TnT",
        "condition": "greater than",
        "value": 1
      }
    },
    {
      "rule-type": "ColumnValues",
      "parameter": {
        "column-name": "Route",
        "condition": "missing delivery less than",
        "value": 5
      }
    }
  ]
}
"""

# Create a data quality ruleset
response = glue.create_data_quality_ruleset(
    Name='RouteThatFitsRules',
    Description='Focus Routes',
    Ruleset=dqdl_rules
)

# Retrieve the ARN of the created ruleset
ruleset_arn = response['RulesetArn']

# Associate the ruleset with a Glue table
glue.put_data_quality_ruleset_association(
    DatabaseName='Improvements',
    TableName='FocusRoutes',  # Ensure this matches the table name used in the DQ rules
    RulesetArn=ruleset_arn
)

# Evaluate the data quality ruleset
response = glue.evaluate_data_quality_ruleset(
    RulesetArn=ruleset_arn,
    TableArn='arn:aws:glue:us-west-2:123456789012:table/Improvements/FocusRoutes'
)

# Print the evaluation results
print(response['EvaluationResult'])
