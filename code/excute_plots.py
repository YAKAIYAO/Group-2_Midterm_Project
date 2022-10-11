import matplotlib.pyplot as plt
import pandas as pd
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


'''Execute pts graph'''
OUT_PATH = os.path.join("plot", "pts.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
ax = fig.add_subplot(1, 1, 1)
plt.scatter(df['pts'], df['name'])
plt.title('Pts Graph')
plt.xlabel('pts')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

'''Execute height graph'''
OUT_PATH = os.path.join("plot", "height.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
ax = fig.add_subplot(1, 1, 1)
plt.scatter(df['height'], df['name'])
plt.title('height Graph')
plt.xlabel('height')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()

'''Execute weight graph'''
OUT_PATH = os.path.join("plot", "weight.png")

df = pd.read_csv(IN_PATH)

fig = plt.figure(figsize = (11,11))
ax = fig.add_subplot(1, 1, 1)
plt.scatter(df['weight'], df['name'])
plt.title('Weight Graph')
plt.xlabel('weight')
plt.ylabel('name') 
plt.savefig(os.path.join(OUT_PATH))
plt.show()