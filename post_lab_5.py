#Question 1
t = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", t.count(2))

#Question 2
t = (10, 20, 30, 40)
num = int(input("Enter a number:"))
if num in t:
    print("Found")
else:
    print("Not found")

#Question 3
t = ('I', 'C', 'T')
s = ''.join(t)   
print("String:", s)

#Question 4
t = (12,13,14,15,16)
print("Maximum:", max(t))
print("Minimum:", min(t))

#Question 5
t = ("Python","Labs")
s = " ".join(t)   
print("Single String:", s)

#Question 6
t = (9,1,5,23,17)
sort = tuple(sorted(t))
print("Sorted tuple:", sort)

#Question 7
t = (1,2,3,4,5)
print("First element:", t[0])
print("Last element:", t[-1])
