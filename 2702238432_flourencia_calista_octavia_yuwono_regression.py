# -*- coding: utf-8 -*-
"""2702238432 - Flourencia Calista Octavia Yuwono - Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qAyrszsD95sdT-XxmzR-XjIXYOHoEYPA
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

#generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

#assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T

#turn y into a column vector
y = y[:, np.newaxis]

#direct least square regression
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A. T,A)),A.T)),y)
print(alpha)

#plot the results
plt.figure(figsize = (10, 8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""Use the pseudoinverse"""

pinv = np.linalg.pinv(A)
alpha = pinv.dot(y)
print(alpha)

"""Use numpy.linalg.lstsq"""

alpha = np.linalg.lstsq(A, y, rcond=None) [0]
print(alpha)

"""Use optimize.curve_fit from scipy"""

#generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

def func(x, a, b) :
  y = a*x + b
  return y

alpha = optimize.curve_fit(func, xdata = x, ydata = y) [0]
print(alpha)