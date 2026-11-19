import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Load the dataset ---
# Replace with your downloaded CSV file path
csv_file = "tractor_make.csv"
df = pd.read_csv(csv_file)

# --- 2. Inspect the data ---
print("First 5 rows:")
print(df.head())
print("\nColumns:", df.columns.tolist())

# --- 3. Pivot the data for heatmap ---
# Rows = County, Columns = Year, Values = Count
pivot_df = df.pivot(index="Tractor Make", columns="Year", values="Count")

print("\nPivoted DataFrame for heatmap:")
print(pivot_df)

# --- 4. Create the heatmap ---
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, annot=True, fmt="g", cmap="YlGnBu")
plt.title("Tractor Registrations by County and Year")
plt.xlabel("Year")
plt.ylabel("County")
plt.tight_layout()
plt.show()
