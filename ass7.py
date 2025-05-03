# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("your_dataset.csv")  # Replace with your actual dataset filename
print("✅ Data loaded successfully!\n")

# Display first few rows
print("📊 First 5 rows of the dataset:")
print(data.head())

# Basic info
print("\n🧾 Dataset Info:")
print(data.info())

# Summary statistics
print("\n📈 Summary Statistics:")
print(data.describe())

# Check for missing values
print("\n❓ Missing Values:")
print(data.isnull().sum())

# -------------------------
# Visualization Examples
# -------------------------

# Histogram of a numeric
