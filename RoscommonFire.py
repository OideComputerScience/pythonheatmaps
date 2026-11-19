import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("RoscommonFire.csv")

# Set station names as row labels
df = df.set_index("Fire Station")

# Create heatmap
plt.figure(figsize=(10,6))

sns.heatmap(
    df,
    annot=True,
    fmt="d",
    cmap="RdPu",
    linewidths=0.5
)

plt.title("Fire Station Callouts – County Roscommon, 2010-2016")
plt.xlabel("Incident Type")
plt.ylabel("Fire Station")

plt.tight_layout()
plt.show()