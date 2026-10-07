class Student:
    subject = "python"
    college = "AUS"
    year = "4th year"
    
students = []

for i in range(10):
    s = Student()
    students.append(s)
    
for student in students:
    print(student.subject,student.college,student.year)
print(f"Total objects: {len(students)}")