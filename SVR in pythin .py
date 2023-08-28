
# Support Vector Regression (SVR)


# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing the Dataset


ataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print(X)
print(y)



