# Find index of the nth element of a 3x3x3 array

import numpy as np

# np.unravel_index(): converts a flat index or array of flat indices into a tuple of coordinate arrays

def findIndex(x, y, z, ele):
    if ele > x*y*z:
        return None
    index = ele-1
    
    x_index = index // (y * z)      # Determine how many full layers of y and z are covered
                                    # by the index to get to the x-coordinate   
    y_index = (index // z) % y      # Remove z-dimension contribution and return the total number of 
                                    # elements in a full layer of y-dimension
    z_index = index % z             # Return position of index in z-dimension

    return (x_index,y_index,z_index)

if __name__ == "__main__":
    ele = int(input("Enter the element: "))
    x_dim = int(input("x-dimension: "))
    y_dim = int(input("y-dimension: "))
    z_dim = int(input("z-dimension: "))
    res = findIndex(x_dim,y_dim,z_dim,ele)
    print(res)
    
    res2 = np.unravel_index(ele,shape=(x_dim,y_dim,z_dim))
    # print(res2)