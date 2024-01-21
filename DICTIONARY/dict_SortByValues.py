# Using lambda, itemgetter() and sorted()

# Using method itemgetter 
from operator import itemgetter

info = [{'name': 'Nolan', 'age': 19},
        {'name': 'Ricky', 'age': 20},
        {'name': 'Harry', 'age': 20}]

get_values = itemgetter('age')

# Sorting by age in ascending order
print(sorted(info, key=get_values))

# Sorting by age in descending order
print(sorted(info, key=get_values, reverse=True))

# Sorting by age and name in ascending order
print(sorted(info, key=itemgetter('age', 'name')))

# Using lambda
# Sorting by age in ascending order
order = lambda i : i['age']
print(sorted(info, key=order))

# Sorting by name in ascending order
order1 = lambda i : (i['age'], i['name'])
print(sorted(info, key=order1)) 