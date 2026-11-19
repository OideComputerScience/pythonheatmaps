import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the dataset
#Replace with your downloaded CSV file path
csv_file = "tractors_by_county.csv"
df = pd.read_csv(csv_file)

#Inspect the data
print("First 5 rows:")
print(df.head())
print("\nColumns:", df.columns.tolist())

#Pivot the data to use for the heatmap
# Rows = County, Columns = Year, Values = Count
pivot_df = df.pivot(index="County", columns="Year", values="Count")

print("\nPivoted DataFrame for heatmap:")
print(pivot_df)

#Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, annot=True, fmt="g", cmap="spring")
plt.title("Tractor Registrations by County and Year")
plt.xlabel("Year")
plt.ylabel("County")
plt.tight_layout()
plt.show()