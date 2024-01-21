# find elements of list 1 at indices present in list 2. 

my_list = [2,8,9,16,10,12,30,3,26]
index_list = [0,4,6,3,5]
def findEl(list1, list2):
    new_list = [list1[i] for i in list2 if i < len(list1)]
    return new_list

print(findEl(my_list,index_list))