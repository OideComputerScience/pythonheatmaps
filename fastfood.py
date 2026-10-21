import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("fastfood.csv")

# set county as index
df = df.set_index("County")

# create heatmap
plt.figure(figsize=(10,8))

sns.heatmap(
    df,
    annot=True,
    fmt="d",
    cmap="Greens",
    linewidths=0.5
)

plt.title("Fast Food Outlets by County in Ireland")
plt.ylabel("County")
plt.xlabel("Brand")

plt.tight_layout()
plt.show()