# OOP : OBJECT-ORIENTED PROGRAMMING

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        grade = 0
        for student in self.students:
            grade += student.get_grade()
            
        return grade / len(self.students)
    
s1 = Student("Nolan", 19, 96)
s2 = Student("Michael", 20, 67)
s3 = Student("Mike", 19, 80)

cmpt_course = Course("CMPT", 2)
cmpt_course.add_students(s1)
cmpt_course.add_students(s2)

print(cmpt_course.get_average_grade())
print(cmpt_course.add_students(s3))