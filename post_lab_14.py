# #question 1
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius *self.radius
    
#     def circumference(self):
#         return 2*3.14*self.radius

# circle = Circle(5)
# print(f"Area of circle: {circle.area()}")
# print(f"Circumference of circle:{circle.circumference()}")

#question 2
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author    
        self.price = price

    def details(self):
        return f"Booktitle: {self.title}, Author: {self.author}, Price: {self.price}"
    
    def discount(self):
        return self.price - 0.1*self.price

book1 = Book("Signals and systems","AK",300)
book2 = Book("COA","MM",400)

print(f"Book 1:{book1.details()}\n",f"book 2:{book2.details()}\n",f"updated price of 2nd book:{book2.discount()}")