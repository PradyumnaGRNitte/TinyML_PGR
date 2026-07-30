import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("D:\\TinyML_Workshop-main\\TinyML_Workshop_PGR\\TinyML_PGR\\Data_Logger\\dataset.csv")

# Select IMU features
features = ["Ax", "Ay", "Az", "Gx", "Gy", "Gz"]

# Normalize
scaler = MinMaxScaler()

df[features] = scaler.fit_transform(df[features])

# Display first five rows
print(df.head())