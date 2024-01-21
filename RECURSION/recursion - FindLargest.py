def findLargest(lis):
    if len(lis) == 0:
        return 0
    elif len(lis) == 1:
        return lis[0]
    max_num = lis[0]
    max_rest = findLargest(lis[1:])
    return max(max_num, max_rest)

if __name__ == "__main__":
    lis = [10,16,9,30,26,8,12,6]
    res = findLargest(lis)
    print(res)