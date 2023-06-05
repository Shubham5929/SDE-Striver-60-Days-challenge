def maximumProfit(prices):
    # Write your code here.
    profit = 0
    miniBuyStock = prices[0]
    for i in range(1,len(prices)):
        if prices[i] > miniBuyStock:
            profit = max(profit,prices[i]-miniBuyStock)
        elif prices[i] < miniBuyStock:
            miniBuyStock = prices[i]
    return profit

prices = [1,2,3,4]
print(maximumProfit(prices))