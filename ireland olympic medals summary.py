import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV (replace the file name if needed)
df = pd.read_csv("ireland_olympic_medals_summary.csv")

# Inspect the data
print(df)

# Pivoting is not necessary since the data is already matrix-like:
# Rows = Sport, Columns = Medal colour, Values = counts
df.set_index("Sport", inplace=True)

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="YlOrBr", cbar_kws={'label': 'Number of Medals'})
plt.title("Ireland Olympic Medals by Sport")
plt.ylabel("Sport")
plt.xlabel("Medal Type")
plt.show()