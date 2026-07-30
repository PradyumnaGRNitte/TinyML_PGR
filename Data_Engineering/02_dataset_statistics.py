import pandas as pd

# Load the dataset
df = pd.read_csv("D:\\TinyML_Workshop-main\\TinyML_Workshop_PGR\\TinyML_PGR\\Data_Logger\\dataset.csv")

# Explore the dataset
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())