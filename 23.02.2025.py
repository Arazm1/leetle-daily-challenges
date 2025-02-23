#54. Best Time to Buy and Sell Stock
#Write a function solve that calculates the maximum profit you can achieve from buying and selling stocks multiple times. You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). The input is an array of prices where prices[i] is the price of a given stock on the ith day.

#Example:
#Input: [7,1,5,3,6,4]
#Output: 7
#Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7. 

#Make sure you return your solution, don't print!


def solve(prices):
    made_profit = 0

    for i in range(1, len(prices)):
        previous_day_price = prices[i-1]
        if prices[i] > previous_day_price:
            made_profit += prices[i] - previous_day_price

    #print(made_profit)
    return made_profit


#solve([7,1,5,3,6,4])
