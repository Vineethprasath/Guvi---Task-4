#Given numbers
Number_list=[10,501,22,37,100,999,87,351]

#To Create 1 empty list for storing the prime number
Prime_number = []

#To take the each number from the given list for validation
for num in Number_list:
    # To Check if the number is greater than 1 (Because 1 is not a prime number)
    if num > 1:
        # To assume the number is prime initially
        is_prime = True
        # To check divisibility of the number from 2 to num-1
        for i in range (2,num):
            if num % i ==0:
                is_prime = False
                #To terminate the for loop after confirming the corresponding number as non-prime number
                break
        #To add the primer number to the primer number list
        if is_prime == True:
            Prime_number.append(num)

#To print the both prime number list and count
print ("Primer number(s):",Prime_number)
print("Total no.of prime numbers in the given list:",len(Prime_number))