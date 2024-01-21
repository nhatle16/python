# Import the module 'operator'
from operator import itemgetter

# With dictionary
data1 = {'key1': 1, 'key2': 2, 'key3': 3}

get_values1 = itemgetter('key1', 'key2')
values1 = get_values1(data1)
print(values1)

# With list of dictionaries
data2 = [{'name': 'Nolan', 'age': 19},
        {'name': 'Harry', 'age': 21},
        {'name': 'Ricky', 'age': 20}]

get_values2 = itemgetter('age')
values2 = [get_values2(person) for person in data2]
print(itemgetter(1)(data2))
print(values2)

# With list of tuples
data3 = [(1, 'one'), (2, 'two'), (3, 'three')]
get_values3 = itemgetter(1)
values3 = get_values3(data3)
print(values3)

option = [itemgetter(0)(ele) for ele in data3]
print(option)