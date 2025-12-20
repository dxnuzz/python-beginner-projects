"""
Program Name: Student Marks Analysis
Description: Inputs marks of 10 students and displays
             maximum, minimum, and average marks. """

marks = []  #list to store marks
sum = 0

#get the input mark of 10 students
for i in range(1, 11):
    mark = int(input(f"Enter mark of student {i} : "))
    marks.append(mark)
    sum += mark

#calculate maximum, minumum and average marks
max_mark = max(marks)
min_mark = min(marks)
average = sum / len(marks)

#display marks
print(f"\nMaximum mark is : {max_mark}")
print(f"Minimum mark is : {min_mark}")
print(f"Average is : {average}\n")

