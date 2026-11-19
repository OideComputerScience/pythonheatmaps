import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gaa_stats.csv")
df.set_index("County", inplace=True)

plt.figure(figsize=(12,8))
sns.heatmap(df, annot=True, cmap="YlGn", linewidths=.5)
plt.title("GAA Titles by County Across Sports")
plt.show()