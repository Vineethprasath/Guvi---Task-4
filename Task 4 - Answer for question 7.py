#given list
integer_list = [100,200,300,400,100,200,300,500,600,700,500,600]

#To Create 1 empty list for storing the prime number
non_repeating_num = []

#To take the each number from the given list for validation and also to check whether non-repeat or not
for num in integer_list:
    if integer_list.count(num) == 1:
        non_repeating_num.append(num)

#To print the given and non-repeating number
print("Given list:",integer_list)
print("Non-repeating number:",non_repeating_num)