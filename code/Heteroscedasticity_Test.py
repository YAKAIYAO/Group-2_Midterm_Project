from sklearn.linear_model import LinearRegression
from statsmodels.stats.diagnostic import het_white
import statsmodels.api as sm
import pandas as pd
import json
import os

IN_PATH = os.path.join("artifacts", "results_integrated.csv")
OUT_PATH = os.path.join("artifacts", "result_regress.json")

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
raw_data = {
	'Test Statistic': white_test[0],
	'Test Statistic p-value': white_test[1],
	'F-Statistic': white_test[2],
	'F-Test p-value': white_test[3]
}

json_data =json.dumps(raw_data)


def write_json(json_data,file_name=OUT_PATH):
	with open(file_name,"w") as outfile:
		outfile.write(json_data)


write_json(json_data)

print(json_data)
print(type(json_data))
#print(dict(zip(labels, white_test)))
