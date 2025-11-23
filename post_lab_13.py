#question 1
with open("example.txt", 'r') as f:
    text = f.read()
lines = text.splitlines()    
words = text.split()         
characters = len(text)            
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

#question 2
filename = "example.txt"   
lines_list = []            
with open(filename, 'r') as file:
    for line in file:
        lines_list.append(line.strip())   
print("List of lines:")
print(lines_list)


#question 3
import csv
filename = r"C:\Users\diyak\Downloads\data-1.csv"   
with open(filename, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#question 4
with open("example.txt", 'r') as f1, open("example1.txt", 'r') as f2, open("merged.txt", 'w') as fout:
    fout.write(f1.read())
    fout.write("\n")          
    fout.write(f2.read())
