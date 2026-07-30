import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load dataset
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "Data_Logger", "dataset.csv")
output_path = os.path.join(base_dir, "Datasets", "dataset_processed.csv")

df = pd.read_csv(input_path)

# Normalize IMU features
features = ["Ax", "Ay", "Az", "Gx", "Gy", "Gz"]
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

# Encode labels
encoder = LabelEncoder()
df["Label"] = encoder.fit_transform(df["Label"])

# Save processed dataset
df.to_csv(output_path, index=False)

print("\n=== Min-Max Scaler Parameters ===")

for feature, dmin, dmax in zip(
        features,
        scaler.data_min_,
        scaler.data_max_):

    print(f"{feature}")
    print(f"  Min : {dmin}")
    print(f"  Max : {dmax}")

print("Processed dataset saved successfully!")