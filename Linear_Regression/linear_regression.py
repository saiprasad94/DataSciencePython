

import numpy as np
import matplotlib            
print (matplotlib.rcParams['backend'])
import matplotlib.pyplot as plt
plt.get_backend()
import pandas as pd

#Importing the data
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

