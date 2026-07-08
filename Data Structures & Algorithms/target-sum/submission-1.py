class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        memo = {}
        def dp(index, currSum):

            if (index, currSum) in memo:
                return memo[(index, currSum)]
            if index == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            
            memo[(index, currSum)] = dp(index +1, currSum+nums[index]) + dp(index +1, currSum-nums[index])
            return memo[(index, currSum)]



        return dp(0,0)