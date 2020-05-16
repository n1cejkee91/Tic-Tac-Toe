# work with the variable 'my_numbers'
#my_numbers = [1, 2, 3, 4, 5]
new_list = [int(i) for i in my_numbers if int(i) % 2 == 0]
print(new_list)