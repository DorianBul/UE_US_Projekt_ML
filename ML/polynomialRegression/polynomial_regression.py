# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('incomePerPositionAtCompany.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Liniowa regresja
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Wielomianowa regresja
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=6)  # optymalny stopien do pokrycia probek
X_poly = poly_reg.fit_transform(X)  # wektor horyzontalny walnij na wielomian^4 stopnia
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# testy
"""
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
"""

# Predykcja za pomoca liniowej regresji
print(lin_reg.predict([[7.5]]))  # tutaj wartosc z enuma jakiegos enuma do pozycji w firmie

# Predykcja za pomoca wielomianowej regresji im wyzszy stopien wielomianu tym lepsze ulozenie co do probek
print(lin_reg_2.predict(poly_reg.fit_transform([[7.5]])))
