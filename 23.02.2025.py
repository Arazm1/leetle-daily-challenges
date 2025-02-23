def solve(prices):
    made_profit = 0

    for i in range(1, len(prices)):
        previous_day_price = prices[i-1]
        if prices[i] > previous_day_price:
            made_profit += prices[i] - previous_day_price

    #print(made_profit)
    return made_profit


#solve([7,1,5,3,6,4])
