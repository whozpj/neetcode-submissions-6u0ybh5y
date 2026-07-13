class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums)/2

        memo = {}

        def dp(index, currSum):
            if currSum == target:
                return True
            if index == len(nums):
                return False
            if currSum > target:
                return False
            if (index, currSum) in memo:
                return memo[(index, currSum)]
                
            take = dp(index + 1, currSum + nums[index])
            skip = dp(index + 1, currSum)

            memo[(index, currSum)] = take or skip
            return memo[(index, currSum)]
        return dp(0,0)

            

            

            