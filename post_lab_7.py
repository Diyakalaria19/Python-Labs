import numpy as np

#Question 1
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

#Question 2
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = np.flip(arr)
print(reversed_arr)

#Question 3
a1 = np.array([11,12,13,14])
a2 = np.array([13,14,15,16])
common = np.intersect1d(a1, a2)
print(common)

#Question 4
a = np.array([1, 2, 3])
repeated = np.repeat(a, 3)
print(repeated)

#Question 5
a = np.array([1, 2, 3, 4, 5])
memory_size = a.nbytes
print("Memory size in bytes:", memory_size)

#Question 6
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
print("Array of zeroes:\n", zeros)
print("Array of ones:\n", ones)

#Question 7
a = np.array([10, 20, 30, 40, 50])
fourth_element = a[3]  
print("4th element:", fourth_element)
