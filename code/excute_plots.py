import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

'''Execute salary graph'''
IN_PATH = os.path.join("artifacts", "results_integrated.csv")
OUT_PATH = os.path.join("plot", "salary.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
plt.barh(df['name'], df['salary'], color = 'maroon')
plt.scatter(df['age'], df['name'])
plt.title('Salary Graph')
plt.xlabel('salary')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

'''Execute age graph'''
OUT_PATH = os.path.join("plot", "age.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
ax = fig.add_subplot(1, 1, 1)
plt.barh(df['name'], df['age'])
plt.title('Age Graph')
plt.xlabel('age')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

'''Execute assist graph'''
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

'''Execute pts by position graph'''
IN_PATH = os.path.join("artifacts", "results_player.csv")
OUT_PATH = os.path.join("plot", "pts_salary.png")

data1 = pd.read_csv(IN_PATH)

sns.scatterplot(data=data1, x="pts", y="salary", hue="position")
plt.savefig(os.path.join(OUT_PATH))
plt.show()





