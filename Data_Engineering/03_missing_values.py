import pandas as pd

# Load dataset
df = pd.read_csv("D:\\TinyML_Workshop-main\\TinyML_Workshop_PGR\\TinyML_PGR\\Data_Logger\\dataset.csv")

# Check missing values
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:", df.isnull().sum().sum())