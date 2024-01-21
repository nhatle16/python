# Calculate the kth coefficient of the binomial expression
def binoCoeff(n, k):
    if k > n:
        return None
    if k == 0 or k == n:
        return 1
    return binoCoeff(n-1,k) + binoCoeff(n-1, k-1)

if __name__ == "__main__":
    res = binoCoeff(5,2)
    print(res)