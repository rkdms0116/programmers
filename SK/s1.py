def mincost(money, costs):
    result = 0
    each_cost = []
    unit_money = [1,5,10,50,100,500]

    for c in range(len(costs)):
        each_cost.append(costs[c]/unit_money[c])
    # print(each_cost)
    
    for i in range(len(costs)):
        m = each_cost.index(sorted(each_cost)[i])
        Q, R = divmod(money, unit_money[m])
        money = R
        result += costs[m] * Q
    # print(min_index)
    return result


# money = 4578
money = 1999
# costs = [1,4,99,35,50,1000]
costs = [2,11,20,100,200,600]
print(mincost(money, costs))