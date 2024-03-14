from typing import List

prices = [7, 1, 5, 6, 3, 4]


def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if buy < sell:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit


print(maxProfit(prices))
