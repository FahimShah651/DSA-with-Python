class Student:                            # Creating a class name student
    def __init__(self, name, marks):      
        self.name = name 
        self.marks = marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)

name = input("Enter student name: ")
marks = []
for i in range(3):
    marks.append(int(input(f"Enter mark {i+1}: ")))

student = Student(name, marks)
print(f"{student.name}'s average marks are: {student.average()}")
