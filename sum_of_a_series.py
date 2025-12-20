"""
This is a program to input numbers until -999 is entered, 
then calculate and print the sum of the entered series. """

#function to calculate the sum of the series
def calculate_sum():
    sum = 0

    while True:
        number = int(input("Enter a number (-999 to stop) : "))

        if number == -999:
            break
        else:
            sum += number
            
    return sum

#display sum
print(f"Sum is : {calculate_sum()}")