# lambda arguments : expression

# Function returns square
def square(x):
    return x**2

# Equivalent lambda function
square_lambda = lambda x : x**2

print(square(10))
print(square_lambda(10))

# Using lambda function to square each number in a list
lis = [1, 2, 3, 4, 5, 6]
res = list(map(square_lambda, lis))
print(res)