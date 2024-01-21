def knapsack(lis_w, lis_p, mass):
    if len(lis_w) == 0 or len(lis_p) == 0 or mass == 0:
        return 0
    
    profit, weight = lis_p[0], lis_w[0]
    value_with_cur = 0
    
    if weight <= mass:
        value_with_cur = profit + knapsack(lis_w[1:], lis_p[1:], mass-weight)
        
    value_without_cur = knapsack(lis_w[1:], lis_p[1:], mass)
    
    return max(value_with_cur, value_without_cur)
    
if __name__ == "__main__":
    lis_p = [2,5,7,8,10]
    lis_w = [6,5,10,3,4]
    mass = 10
    
    res = knapsack(lis_w, lis_p, mass)
    print(res)