import pandas as pd

# Load dataset
df = pd.read_csv("D:\\TinyML_Workshop-main\\TinyML_Workshop_PGR\\TinyML_PGR\\Data_Logger\\dataset.csv")

# Count duplicate rows
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

# Remove duplicates
df = df.drop_duplicates()

# Verify dataset
print("New Shape:", df.shape)