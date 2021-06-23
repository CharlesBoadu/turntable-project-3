from Course import Course
import datetime

class Student(Course):

    def __init__(self, firstName, lastName, dateOfBirth, administrationNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.administrationNumber = administrationNumber


student1 = Student("Charles", "Osei", datetime.datetime(1999, 3, 6), 1234)
student2 = Student("Frank", "Manu", datetime.datetime(1999, 4, 9), 4321)
student3 = Student("Desmond", "Tetteh", datetime.datetime(2001, 5, 2), 1111)
student4 = Student("John", "Tangkobo", datetime.datetime(2000, 5, 22), 1212)
student5 = Student("Francisca", "Opoku", datetime.datetime(1995, 5, 24), 1255)
student6 = Student("Manu", "Kofi", datetime.datetime(2001, 2, 5), 1921)
student7 = Student("Samuel", "Kofi", datetime.datetime(1999, 10, 22), 2020)
student8 = Student("Matilda", "Afia", datetime.datetime(1999, 11, 11), 1876)
student9 = Student("Pearl", "Owusu", datetime.datetime(1999, 8, 24), 2222)
student10 = Student("Kwame", "Safo", datetime.datetime(1997, 10, 3), 3333)


print("\tLIST OF STUDENTS WITH THEIR PERSONAL DETAILS")
num = 1
for studentDetails in (student1, student2, student3, student4, student5, student6, student7, student8, student9, student10):
    print(f"Student {num} Details:")
    print(f"FirstName: {studentDetails.firstName}, LastName: {studentDetails.lastName}, Date Of Birth: {studentDetails.dateOfBirth}, Administration Number: {studentDetails.administrationNumber}") 
    print("\n")
    num += 1

    
print("\n")
course1 = Course("English", 1)
course2 = Course("Mathematics", 2)
course3 = Course("Social Studies", 3)
course4 = Course("Economics", 4)
course5 = Course("Geography", 5)
course6 = Course("Elective Maths", 6)
course7 = Course("French", 7)
course8 = Course("Literature", 8)
course9 = Course("Science", 9)
course10 = Course("Information Communication and Technology", 10)

i = 0
print("\tPER STUDENT, THESE ARE COURSES EACH IS ENROLLED IN")
for course in (course2, course4, course5, course6, course9, course8, course7, course1, course10, course3):
    firstNames = ["Charles", "Frank", "Desmond", "John", "Francisca", "Manu", "Samuel", "Matilda", "Pearl", "Kwame"]
    print(f"{firstNames[i]} is enrolled in {course.name} with Course Number of {course.number}")
    i += 1
    if (i == 10):
        break
