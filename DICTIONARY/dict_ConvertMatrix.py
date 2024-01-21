# Converting a Matrix to Dictionary
# Using dictionary comprehension

# Initialize a matrix
matrix = [[1, 2, 3],
          [2, 4, 6],
          [5, 7, 9]]

res_dict = {idx + 1: matrix[idx] for idx in range(len(matrix))}

print(f"Original matrix: {matrix}")
print(f"Matrix as dictionary: {res_dict}")