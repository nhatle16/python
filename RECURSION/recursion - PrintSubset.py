def allSubset(lis):
    if len(lis) == 0:
        print(subset)
        return 
    subset = []
    for i in lis:
        subset.append(i)
    print(subset)
    return allSubset(lis[1:])

def print_all_subsets(arr, subset, index):
    # Base case: If we've processed all elements, print the current subset.
    if index == len(arr):
        print(subset)
        return

    # Include the current element in the subset and move to the next index.
    print_all_subsets(arr, subset + [arr[index]], index + 1)

    # Exclude the current element from the subset and move to the next index.
    print_all_subsets(arr, subset, index + 1)


if __name__ == "__main__":
    lis = [6,1,0,9,2]
    # allSubset(lis)
    print_all_subsets(lis, [], 0)