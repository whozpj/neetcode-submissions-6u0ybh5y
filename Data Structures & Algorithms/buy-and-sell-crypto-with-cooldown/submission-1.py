class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you can either buy or sell
        #if you sell, you must enter a cooldown (i+2)

        #memo = (index, buying):profit
        memo = {}

        def dfs(index, buying):
            
            #base case: out of bounds so return 0
            if index >= len(prices):
                return 0
            
            #already seen
            if (index,buying) in memo:
                return memo[(index,buying)]
            
            doNothingPrice= dfs(index+1, buying) 

            #buy if in selling mode
            if not buying:
                buyingPrice = -prices[index] + dfs(index + 1, not buying)
                profit = max(doNothingPrice, buyingPrice)
            else:
                sellingPrice = prices[index] + dfs(index + 2, not buying)
                profit = max(doNothingPrice, sellingPrice)

            memo[(index, buying)] = profit
            return profit

            
        return dfs(0, False)
