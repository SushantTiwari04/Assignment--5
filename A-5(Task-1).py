student_marks = {"Alice": 85,"Bob": 78,"Charlie": 92,"David":74,"Eve":90}
name = input("Enter the student's name:")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")