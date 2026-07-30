import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("D:\\TinyML_Workshop-main\\TinyML_Workshop_PGR\\TinyML_PGR\\Data_Logger\\dataset.csv")

# Create encoder
encoder = LabelEncoder()

# Encode labels
df["Label"] = encoder.fit_transform(df["Label"])

# Display encoded dataset
print(df.head())

# Display mapping
print("\nLabel Mapping:")
for index, label in enumerate(encoder.classes_):
    print(f"{label} -> {index}")