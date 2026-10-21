#1. Import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2.Load csv with pandas
df = pd.read_csv("licences_by_county.csv")

# 3. Set County as index
df = df.set_index("County")

# create heatmap
plt.figure(figsize=(12,10))
# 4. Pass the DataFrame to seaborn
sns.heatmap(
    df,
    annot=True,
    fmt="d",
    cmap="YlOrRd", #5. Add labels, scale and colourmap
    cbar_kws={"label": "Number of Driving Licences"}
)

plt.title("Driving Licences by County (2013–2024)")
plt.xlabel("Year")
plt.ylabel("County")

plt.tight_layout()
plt.show()