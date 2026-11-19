# livestock_heatmap.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Load the dataset ---
# Replace 'AAA09_number_of_livestock_in_june.csv' with your downloaded CSV file path
csv_file = "livestock_in_june2.csv"
df = pd.read_csv(csv_file)

# --- 2. Inspect the data ---
print("First 5 rows of the dataset:")
print(df.head())

# Check column names to make sure they match the pivot
print("\nColumns in dataset:", df.columns.tolist())

# --- 3. Pivot the data for heatmap ---
# Adjust column names as needed to match the dataset
# Assume columns: 'Year', 'Livestock type', 'Count'
pivot_df = df.pivot(index="Livestock Type", columns="Year", values="Count")

print("\nPivoted DataFrame for heatmap:")
print(pivot_df)

# --- 4. Create the heatmap ---
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt="g", cmap="viridis", linewidth = 0.5)
plt.title("Livestock Counts by Type and Year in 000s")
plt.ylabel("Livestock Type")
plt.xlabel("Year")
plt.tight_layout()
plt.show()