# Question 1
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Line Plot")
# plt.show()

#Question 2
# import matplotlib.pyplot as plt
# x = [11, 12, 13, 14, 15]
# y1 = [1, 4, 9, 16, 25]
# y2 = [1, 2, 3, 4, 5]
# plt.plot(x, y1, label="y = x^2")
# plt.plot(x, y2, label="y = x")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Two Lines on Same Plot")
# plt.legend()
# plt.show()

#Question 3
import matplotlib.pyplot as plt
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(languages, popularity)
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.show()
