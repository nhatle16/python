# Students' dictionary
harry = {'name': 'Harry Potter',
         'quiz': [80, 90, 90, 95],
         'midterm': [85, 90],
         'final': [93.86]
         }

nolan = {'name': 'Nolan Le',
         'quiz': [90, 96, 92, 95],
         'midterm': [92, 96],
         'final': [90.16]
         }

henry = {'name': 'Henry Masch',
         'quiz': [87, 83, 90, 89],
         'midterm': [85, 85],
         'final': [89.24]
         }

macey = {'name': 'Macey Blose',
         'quiz': [83, 80, 86, 82],
         'midterm': [83, 87],
         'final': [77.26]
         }

# Function calculates the average of a section
def calculate_ave(grade_lis):
    total = sum(grade_lis)
    return total / len(grade_lis)

# Function calculates the final average grade of a student
def final_ave(stu):
    quiz = calculate_ave(stu['quiz'])
    midterm = calculate_ave(stu['midterm'])
    final = calculate_ave(stu['final'])
    
    return 0.2*quiz + 0.3*midterm + 0.5*final

# Function determines the letter grade
def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
# Function calculates the final grade in class
def class_av(stu_lis):
    result = []
    for stu in stu_lis:
        stu_ave = final_ave(stu)
        result.append(stu_ave)
        
    return calculate_ave(result)

stu_lis = [harry, nolan, henry, macey]

for stu in stu_lis:
    print(stu['name'])
    print('-' * 30)
    print("%s's grade: %s" % (stu['name'], final_ave(stu)))
    print("%s's letter grade: %s" % (stu['name'], letter_grade(final_ave(stu))))
    print()
    
print("Class average is: %s" % class_av(stu_lis))
print("Letter grade of class is: %s" % letter_grade(class_av(stu_lis)))