my_list = {char for char in range(0, 100)}
my_list2 = {char ** 2 for char in range(0, 100)}
my_list3 = [char ** 2 for char in range(0, 100) if char % 2 == 0]

# print(my_list2, "*********")
# print(my_list3, "*********")
simple_dict = {"bob": 2, "frank": 3}

my_dict = {key: value ** 2 for key, value in simple_dict.items()}
print(my_dict)
