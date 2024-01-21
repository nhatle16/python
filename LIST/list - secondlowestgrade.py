def secondLowest(students):
    lowest = float('inf')
    for stu in students:
        if stu[1] < lowest:
            lowest = stu[1]
            
    sec_lowest = float('inf')
    for stu in students:
        if stu[1] < sec_lowest and stu[1] != lowest:
            sec_lowest = stu[1]
            
    second_lowest = [stu for stu in students if stu[1] == sec_lowest]
    second_lowest.sort()

    print(second_lowest)

def main():
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    secondLowest(students)

main()