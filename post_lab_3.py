#Question 1
user = input("Enter a string: ")
rev = "".join(reversed(user))
print("Reversed string:", rev)

#Question 2
user = input("Enter a string: ")
rev = "".join(reversed(user))
if user == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Question 3
user = input("Enter a string: ")
if user.isdigit():
    print("Only digits")
else:
    print("It has other characters too")

#Question 4
user = input("Enter a sentence: ")
words = user.split()
longest = max(words, key=len)
print("Longest word:", longest)

#Question 5
user = input("Enter a sentence: ")
words = user.split()        
last_word = words[-1]           
print("Length of last word:", len(last_word))
