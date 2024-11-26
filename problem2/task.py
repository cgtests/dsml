"""
Perform the following operations using Python on the Telecom_Churn
dataset. Compute and display summary statistics for each feature available
in the dataset using separate commands for each statistic. (e.g. minimum
value, maximum value, mean, range, standard deviation, variance and
percentiles).
"""
import pandas as pd
# Load the Telecom Churn dataset
telecom_churn_path = "../datasets/Telecom Churn.csv"
telecom_df = pd.read_csv(telecom_churn_path)

# Display the first few rows and dataset info to understand its structure
telecom_df.head(), telecom_df.info()
# Selecting only numeric columns for statistical analysis
numeric_features = telecom_df.select_dtypes(include=['float64', 'int64']).columns

# Initialize a dictionary to hold statistics
statistics = {}

# Compute and store statistics for each numeric feature
for feature in numeric_features:
    stats = {
        "min": telecom_df[feature].min(),
        "max": telecom_df[feature].max(),
        "mean": telecom_df[feature].mean(),
        "range": telecom_df[feature].max() - telecom_df[feature].min(),
        "std_dev": telecom_df[feature].std(),
        "variance": telecom_df[feature].var(),
        "25th_percentile": telecom_df[feature].quantile(0.25),
        "50th_percentile": telecom_df[feature].quantile(0.50),
        "75th_percentile": telecom_df[feature].quantile(0.75),
    }
    statistics[feature] = stats

# Display computed statistics for each numeric feature
statistics

