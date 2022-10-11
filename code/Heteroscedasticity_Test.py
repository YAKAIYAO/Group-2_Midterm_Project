from sklearn.linear_model import LinearRegression
from statsmodels.stats.diagnostic import het_white
import statsmodels.api as sm
import pandas as pd
import os

IN_PATH = os.path.join("artifacts", "results_integrated.csv")

data = pd.read_csv(IN_PATH)
data.info()

#define response variable
y = data['salary']

#define predictor variables
x = data[['height', 'weight','age', 'assist', 'pts']]

#add constant to predictor variables
x = sm.add_constant(x)

#fit regression model
model = sm.OLS(y, x).fit()

#perform White's test
white_test = het_white(model.resid,  model.model.exog)

#define labels to use for output of White's test
labels = ['Test Statistic', 'Test Statistic p-value', 'F-Statistic', 'F-Test p-value']

#print results of White's test
print(dict(zip(labels, white_test)))