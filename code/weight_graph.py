import matplotlib.pyplot as plt
import pandas as pd
import os

IN_PATH = os.path.join("artifacts", "results_integrated.csv")
OUT_PATH = os.path.join("plot", "weight.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
ax = fig.add_subplot(1, 1, 1)
plt.scatter(df['weight'], df['name'])
plt.title('Age')
plt.xlabel('weight')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

