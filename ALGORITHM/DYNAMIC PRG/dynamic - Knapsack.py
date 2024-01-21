def knapsack(lis_w, lis_p, weight):
    if len(lis_w) == 0 or len(lis_p) == 0 or weight == 0:
        return 0
    item_w, item_p = lis_w[0], lis_p[0]
    
    if item_w < weight:
        value_with_cur = item_p + knapsack(lis_w=lis_w[1:], lis_p=lis_p[1:],weight=weight-item_w)
    else:
        value_with_cur = 0
    value_without_cur = knapsack(lis_w=lis_w[1:],lis_p=lis_p[1:],weight=weight)
    
    return max(value_with_cur, value_without_cur)

if __name__ == "__main__":
    lis_p = [2,5,7,8,10]
    lis_w = [6,5,10,3,4]
    weight = 15
    
    res = knapsack(lis_w, lis_p, weight)
    print(res)