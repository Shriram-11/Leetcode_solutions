'''
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


'''

# Dynamic Programming Approach


def best(prices):
    # set max profit to 0 and purchase to the first element
    profit, purchase = 0, prices[0]
    # for loop from next date to the last date
    for i in range(1, len(prices)):
        # if we sell stock on ith day the profit will be purchase-current
        profit = max(profit, prices[i]-purchase)
        # if the current prices is less than last purchase prices we purchase on the current date
        purchase = min(purchase, prices[i])
    return profit


print(len(str(len(str(len("Python"))))))
