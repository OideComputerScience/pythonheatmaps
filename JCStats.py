import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv("JCStats.csv")

# Remove extra spaces from column headings
df.columns = df.columns.str.strip()

# Inspect the data
print(df.head())

# Prepare the data
# Combine subject and level into one label
df["Subject_Level"] = df["Subject"].str.strip() + " (" + df["Level"] + ")"

# Select the grade columns
grades = ["DN", "HM", "MT", "AD", "PA", "NG"]

# Create the DataFrame for the heatmap
pivot_df = df.set_index("Subject_Level")[grades]

#Create the heatmap
plt.figure(figsize=(12, 10))

sns.heatmap(
    pivot_df,
    annot=True,
    fmt=".1f",
    cmap="Greens",
    linewidths=0.5
)

plt.title("Junior Cycle Grade Distribution 2026")
plt.xlabel("Grade")
plt.ylabel("Subject and Level")
plt.tight_layout()
plt.show()