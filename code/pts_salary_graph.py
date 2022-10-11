import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

IN_PATH = os.path.join("artifacts", "results_player.csv")
OUT_PATH = os.path.join("plot", "pts_salary.png")

data1 = pd.read_csv(IN_PATH)

sns.scatterplot(data=data1, x="pts", y="salary", hue="position")
plt.show()


