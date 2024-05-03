def maxProfit(prices):
    buy_price, profit = prices[0], 0
    for price in prices:
        if price < buy_price:
            buy_price = price
        if price - buy_price > profit:
            profit = price - buy_price
    return profit

prices = [7,6,4,3,1]

print(maxProfit(prices))