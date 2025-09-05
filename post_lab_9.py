import pandas as pd

# #Question 1
series1 = pd.Series([12,13,14,15,16])
series2 = pd.Series([1,2,3,4,5])
print("Addition: ",series1+series2)
print("Subtraction: ",series1-series2)
print("Multiplication: ",series1*series2)
print("Division: ",series1/series2)

#Question 2
data = {'a': 12,'b': 13,'c': 14,'d': 15}
print(data)
series = pd.Series(data)
print(series)

#Question 3
import numpy as np
data1 = [10, 20, 30, 40]
series1 = pd.Series(data1)
print("Series from list: ",series1)

data2 = np.array([1, 2, 3, 4, 5])
series2 = pd.Series(data2)
print("Series from numpy array: ",series2)

data3 = {'p': 10, 'q': 20, 'r': 30}
series3 = pd.Series(data3)
print("Series from dictionary: ",series3)

#Question 4
series1 = pd.Series([11,12,13,14])
series2 = pd.Series([15,16,17,18])

vertical_stack = pd.concat([series1, series2])
print("Vertical Stack: ",vertical_stack)
horizontal_stack = pd.concat([series1, series2], axis=1)
print("\nHorizontal Stack: ",horizontal_stack)