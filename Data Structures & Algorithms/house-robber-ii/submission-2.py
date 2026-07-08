class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:]

        def dfs(i, n, memo):

            if i >= len(n):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i + 1, n, memo), n[i] + dfs(i + 2, n, memo))
            return memo[i]

        return max(dfs(0, nums1, {}),dfs(0,nums2, {}))
            