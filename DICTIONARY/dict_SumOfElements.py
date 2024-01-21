def calSum(dict):
    sum = 0
    for i in dict.keys():
        sum += dict[i]
        
    return sum

if __name__ == "__main__":
    my_dict = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4}
    res = calSum(my_dict)
    
    print(res)