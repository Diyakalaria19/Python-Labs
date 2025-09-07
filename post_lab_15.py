import sqlite3

conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS student_record")

cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL,
                    PRIMARY KEY (Enrollment, Subject)
                )''')

conn.commit()

student_record = [
    (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
    (92301733016,'ASHUTOSH KUMAR SINGH','DBMS',88),
    (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
    (92301733017,'HARSH VISHALBHAI TRIVEDI','Maths',92),
    (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
    (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','OS',89)
]

cursor.executemany('''INSERT OR IGNORE INTO student_record (Enrollment, name, Subject, Mark) 
                      VALUES (?, ?, ?, ?)''', student_record)
conn.commit()

cursor.execute('SELECT * FROM student_record')
rows = cursor.fetchall()
print("All Student Records (multiple subjects allowed):")
for row in rows:
    print(row)

cursor.execute('SELECT name, Subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

cursor.execute('''UPDATE student_record SET Mark = 98 
                  WHERE name = 'ASHUTOSH KUMAR SINGH' AND Subject = 'PWP' ''')
conn.commit()

cursor.execute('SELECT name, Subject, Mark FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
updated_marks = cursor.fetchall()
print("\nUpdated Marks for ASHUTOSH KUMAR SINGH:")
for mark in updated_marks:
    print(mark)

cursor.execute('''DELETE FROM student_record 
                  WHERE name = 'HARSH VISHALBHAI TRIVEDI' AND Subject = 'Maths' ''')
conn.commit()

cursor.execute('SELECT * FROM student_record WHERE name = "HARSH VISHALBHAI TRIVEDI"')
remaining = cursor.fetchall()
print("\nRemaining records for HARSH VISHALBHAI TRIVEDI:")
for r in remaining:
    print(r)

cursor.execute('''SELECT AVG(Mark) FROM student_record''')
avg_mark = cursor.fetchone()[0]
print(f"\nThe average mark across all subjects is: {avg_mark:.2f}")

conn.close()
