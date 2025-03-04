#To get the input in the console
num = int(input("Enter the number:"))

#To convert the integer to string to identify the first and last digit of the entered number
num_str = str(num)

#To convert the string to integer for proceeding the addition
first_digit = int(num_str[0])
last_digit = int(num_str[-1])

#To proceed the sum of first and last digit of the number only if the entered number has more than 1 digit
if len(num_str) > 1:
    Sum_of_first_and_last_digits = first_digit + last_digit
    print("Sum of first and last digit of the entered number is:",Sum_of_first_and_last_digits)
else:
    print("Please enter more than 1 digit number!!")