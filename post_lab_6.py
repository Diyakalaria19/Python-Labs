#Question 1
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

#Question 2
num = int(input("Enter a number: "))
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print("Sum of natural numbers from 1 to", num, "is:", total)

# Question 3
#method 1
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)

#method2
num = input("Enter a number: ")
count = len(num)   
print("Number of digits:", count)


# Question 4
num = int(input("Enter a numbre: "))
last = num % 10
first = num
while first >= 10:
    first //= 10
print("First digit:", first)
print("Last digit:", last)

# Question 5
num = input("Enter a number: ")
swap = num[-1] + num[1:-1] + num[0]
print("Before swapping:", num)
print("After swapping:", swap)

# Question 6
num = int(input("Enter a number: "))
mul = 1
while num > 0:
    digit = num % 10
    mul *= digit
    num //= 10
print("Product of digits:", mul)

# Question 7
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num //= 10
print("Reverse number is:", rev)
