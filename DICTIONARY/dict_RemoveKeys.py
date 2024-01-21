# Using split(), loop and replace()

my_str = "I love using Python for coding"

my_dict = {'love': 10, 'for': 15}

for key in my_dict:
    if key in my_str.split():
        my_str = my_str.replace(key, "")
        
print(my_str)