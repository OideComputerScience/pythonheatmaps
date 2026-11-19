import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the data from csv file
df = pd.read_csv("state_exams_a.csv")

#Clean the data by removing blank spaces after names
df.columns = df.columns.str.strip()
df["Subject"] = df["Subject"].str.strip()

#Set the data for the heatmap
grades = ["1", "2", "3", "4", "5", "6", "7", "8"]

heatmap_data = df.set_index("Subject")[grades]

# 4. Create the heatmap
plt.figure(figsize=(12, 14))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".1f",
    cmap="RdPu",
    linewidths=0.5
)

plt.title("State Examination Results - Ordinary Level")
plt.xlabel("Grade")
plt.ylabel("Subject")

plt.tight_layout()
plt.show()
