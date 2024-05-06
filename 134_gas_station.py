def canCompleteCircuit(gas, cost):
    if sum(gas) - sum(cost) < 0:
        return -1

    tank, start_i = 0, 0
    for i in range(len(gas)):
        tank = gas[i] - cost[i]

        if tank < 0:
            start_i = i + 1
            tank = 0
    
    return start_i