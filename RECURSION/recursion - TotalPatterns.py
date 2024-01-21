# Function that receives 2 inputs n and m and outputs the number of unique paths
# from the top left corner to bottom right corner of a n x m grid

def totalPatterns(n, m):
    # if there is a dimension equals 1
    if n == 1 or m == 1:
        return 1
    else: 
        return totalPatterns(n-1,m) + totalPatterns(n, m-1)
    