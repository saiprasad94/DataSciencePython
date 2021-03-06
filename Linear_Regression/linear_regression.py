


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the data
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

# Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X,Y, test_size = 1/3, random_state = 0)



#Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)


# Predecting the Test set Results
y_pred =regressor.predict(X_test)

#visualising the Training set results
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()
plt.show()


#visualising the Test set results
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()