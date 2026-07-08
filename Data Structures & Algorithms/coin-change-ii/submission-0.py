class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dp(index, amount):
            if (index, amount) in memo:
                return memo[(index, amount)]

            # Successfully formed amount
            if amount == 0:
                return 1

            # Out of coins or amount went negative
            if index >= len(coins) or amount < 0:
                return 0

            # Choice 1: use current coin again
            use = dp(index, amount - coins[index])

            # Choice 2: skip current coin
            skip = dp(index + 1, amount)

            memo[(index, amount)] = use + skip
            return memo[(index, amount)]

        return dp(0, amount)