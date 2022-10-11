import matplotlib.pyplot as plt
import pandas as pd
import os

IN_PATH = os.path.join("artifacts", "results_integrated.csv")
OUT_PATH = os.path.join("plot", "assist.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
ax = fig.add_subplot(1, 1, 1)
plt.scatter(df['assist'], df['name'])
plt.title('Assist Graph')
plt.xlabel('assist')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

