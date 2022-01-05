def change(coins, amount):
    result = [amount+1] * (amount+1)
    coins_results = [[] for _ in range(amount+1)]
    result[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin and result[i - coin] + 1 < result[i]:
                result[i] = result[i-coin] + 1
                coins_results[i] = coins_results[i-coin] + [coin]
    if result[amount] == amount+1:
        return []

    return coins_results[amount]

def all_change(coins, amount):
    res = []

    def backtrack(end, remain, cur_result):
        if end < 0: return
        if remain == 0:
            res.append(cur_result)
            return
        if remain >= coins[end]:
            backtrack(end, remain - coins[end], cur_result + [coins[end]])
        backtrack(end - 1, remain, cur_result)

    backtrack(len(coins) - 1, amount, [])
    return res

