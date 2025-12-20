"""
This ia a program to input five marks of a student 
and display their grades. """

#function to calculate grade
def grade_calculate(mark):
    if mark > 75:
        return 'A'
    elif mark >= 65:
        return 'B'
    elif mark >= 55:
        return 'C'
    elif mark >= 45:
        return 'S'
    else:
        return 'F'
    
    
grades = [] #list to store grades

#get input of 5 marks and assign grades    
for i in range(1, 6):
    mark = int(input(f"Enter mark {i} : "))
    grade = grade_calculate(mark)
    grades.append(grade)

#display grades
print("\nGrades...")
for j in range(len(grades)):
    print(f"Grade of mark {j+1} is : {grades[j]}")

