#Given numbers
Number_list=[10,501,22,37,100,999,87,351]

#Created 2 empty list for storing the even and odd numbers
Even = []
Odd = []

#Condition to differentiate the odd and even numbers
for num in Number_list:
    if num %2 ==0:
        Even.append(num)
    else:
        Odd.append(num)

#To print the given number list, odd and even numbers list
print("Given Number list:",Number_list)
print("Even numbers:",Even)
print("Odd Numbers:",Odd)