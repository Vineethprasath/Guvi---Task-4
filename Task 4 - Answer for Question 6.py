#given list
list_1 = [100,200,300,400,500]
list_2 = [500,600,700,800,900]
list_3 = [800,1000,1100,1200,2000,3000]

#To add all the 3 lists into 1 list
combination_all_list= list_1 + list_2 + list_3

#Created empty list for storing the duplicate values
duplicate_num = []

#condition to find the duplicates
for num in combination_all_list:
    if combination_all_list.count(num) != 1 and num not in duplicate_num:
        duplicate_num.append(num)

#To print the given list and duplicate values
print("Given list:",list_1,list_2,list_3)
print("duplicate number:",duplicate_num)
