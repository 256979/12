# def factorialgit add(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n -1)
#
# print(factorial(99))
# def max_profit(stock_prices):
#     nb_vals = len(stock_prices)
#     max_profit = 0
#     for i in range(nb_vals):
#         for j in range(i + 1, nb_vals):
#             max_profit = max(max_profit, stock_prices[j] - stock_prices[i])
#     return max_profit

def max_profit(stock_prices):
    nb_vals = len(stock_prices)
    if nb_vals <= 1:
        return 0
    left_profit = max_profit(stock_prices[:nb_vals // 2])
    right_profit = max_profit(stock_prices[nb_vals // 2:])
    left_min = min(stock_prices[:nb_vals // 2])
    right_max = max(stock_prices[nb_vals // 2:])
    return max(left_profit, right_profit, right_max - left_min)
print(max_profit( [15 , 48 , 12 , 11 , 5, 8]))