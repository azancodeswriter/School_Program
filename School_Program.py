print("                   School Program                  ")
print("_____________________________________________________")
print()
print("------------- Kindly enter the details --------------")
print()

num_students = int(input("Enter the number of students for whom you want to collect data: "))

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        return total, avg
    
    def result(self):
        _, avg = self.avg()
        return "Pass" if avg >= 40 else "Fail"

students = []

for s in range(num_students):
    print()
    print(f"     Kindly enter the details of student {s+1}")
    name = input("Enter the name of the student: ")
    student_marks = []
    for i in range(3):
        mark = int(input(f"Enter the marks of subject {i+1}: "))
        student_marks.append(mark)
    students.append(Student(name, student_marks))

# Print results
with open("practice.txt", "a") as f:
    for student in students:
        total, avg = student.avg()
        result = student.result()
        f.write(f"Name: {student.name}, Total: {total}, Average: {avg}, Result: {result}\n")
        print(f"Name: {student.name}, Total: {total}, Average: {avg}, Result: {result}") 