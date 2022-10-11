import matplotlib.pyplot as plt
import pandas as pd
import os

IN_PATH = os.path.join("artifacts", "results_integrated.csv")
OUT_PATH = os.path.join("plot", "salary.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (110,11))
plt.barh(df['name'], df['salary'], color = 'maroon')
plt.scatter(df['age'], df['name'])
plt.title('salary')
plt.xlabel('salary')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

