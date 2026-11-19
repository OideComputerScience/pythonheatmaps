import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv("JCSits.csv")

# Remove extra spaces from column headings
df.columns = df.columns.str.strip()

# 2. Inspect the data
print(df.head())

# 3. Pivot the data
pivot_df = df.pivot(
    index="Subject",
    columns="Level",
    values="Total"
)

# 4. Create the heatmap
plt.figure(figsize=(10, 10))

sns.heatmap(
    pivot_df,
    annot=True,
    fmt="g",
    cmap="Blues",
    linewidths=0.5
)

plt.title("Junior Cycle Subject Popularity 2026")
plt.xlabel("Level")
plt.ylabel("Subject")
plt.tight_layout()
plt.show()