def sumOfList(lis):
    if len(lis) == 0:
        return None
    total = 0
    for ele in lis:
        if isinstance(ele, list):
            total += sumOfList(ele)
        else:
            total += ele
    return total

if __name__ == "__main__":
    lis = [1,5,[7,23,[1,4,5],6],10,16]
    res = sumOfList(lis)
    print(res)