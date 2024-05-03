def maxProfit(prices):
    if len(prices) < 2:
        return 0
    
    profit = 0
    buy = 0
    while buy < len(prices) - 1:
        if prices[buy] < prices[buy + 1]:
            profit += prices[buy + 1] - prices[buy]
        buy += 1
    
    return profit


prices = [7,6,4,3,1]
print(maxProfit(prices))