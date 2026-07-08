class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        


        def dp(amt, memo):

            #base cases
            if amt in memo:
                return memo[amt]

            if amt == 0:
                return 0


            currentMin = float('inf')
            for coin in coins:
                if amt - coin >= 0:
                    currentMin = min(1 + dp(amt-coin, memo), currentMin)
            
            memo[amt] = currentMin
            return currentMin

        result = dp(amount, {})

        if result == float('inf'):
            return -1
        return result