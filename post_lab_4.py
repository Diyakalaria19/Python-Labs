#Question 1
import math
numbers = [1,3,5,7,9]
product = math.prod(numbers)     
print("Product of list elements:", product)

#Question 2
numbers = [11, 12, 13, 14, 15]
print("Largest number:", max(numbers))   

#Question 3
user = [1, 2, 2, 3, 4, 4, 5]
removed = list(set(user))   
print("List after removing duplicates:", removed)

#Question 4
from collections import Counter
items = ['yes', 'no', 'yes', 'yes', 'no', 'yes']
freq = Counter(items)
print(freq)

#Question 5
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
common = list(set(l1).intersection(l2))
print("Common items:", common)

#Question 6
nums = [1, 2, 3, 4]
single_int = ""
for n in nums:
    single_int = single_int + str(n)
single_int = int(single_int)   
print(single_int)
