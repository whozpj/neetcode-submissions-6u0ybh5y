class Solution:
    def lengthOfLIS(self, nums):

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            ans = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))

            memo[i] = ans
            return ans

        result = 0

        for i in range(len(nums)):
            result = max(result, dfs(i))

        return result