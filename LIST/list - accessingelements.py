my_list = [9,4,5,8,10,14]
index_list = [2,3,6,4]

new_list = [my_list[i] for i in index_list if i < len(my_list)]

print(new_list)