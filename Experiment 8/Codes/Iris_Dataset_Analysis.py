"""
This script loads the Iris dataset, provides an overview of the dataset, 
and displays various statistics and details about the data.

Steps included:
1. **Dataset Overview**: The first few rows of the dataset are displayed to get an idea of its structure.
2. **Data Types and Missing Values**: Information about the data types of each column and the presence of any missing values is printed.
3. **Summary Statistics**: Summary statistics such as count, mean, standard deviation, minimum, maximum, and percentiles are calculated and displayed for each numeric column.
4. **Count of Unique Values**: Displays the count of unique values in each column.
5. **Class Distribution**: The distribution of the target variable (`species`) is displayed to show how many samples exist for each species in the dataset.
6. **Detailed Statistics**: Provides detailed statistics, including mean, standard deviation, minimum, and maximum values for all features (both numerical and categorical).

The Iris dataset is a well-known dataset in the machine learning community, commonly used for classification tasks. This script provides a quick overview and insight into the structure and characteristics of the data.

Libraries Used:
- **pandas**: For data manipulation and analysis.
- **seaborn**: For loading the Iris dataset and visualizing the data (although no plots are generated in this script).

Output:
- Overview of the first few rows of the dataset.
- Information about data types and missing values.
- Summary statistics for numeric columns.
- Count of unique values for each column.
- Class distribution of the target variable (`species`).
- Detailed statistical summary for both numerical and categorical features.

Author: Madhurima Rawat
Date: November 23, 2024
"""

# Import libraries
import pandas as pd
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Print dataset overview
print("Iris Dataset Overview:")
print(iris.head())  # Shows first few rows of the dataset

# Print data types and number of missing values
print("\nData Types and Missing Values:")
print(iris.info())

# Summary statistics
print("\nSummary Statistics:")
print(iris.describe())  # Provides count, mean, std, min, max, and quantiles

# Count of unique values in each column
print("\nCount of unique values in each column:")
print(iris.nunique())

# Class distribution (Count of each species)
print("\nClass Distribution (Species counts):")
print(iris["species"].value_counts())

# Display additional statistics (e.g., mean, std, min, max)
print("\nDetailed Statistics (including mean, std, min, max for each feature):")
print(iris.describe(include="all"))
