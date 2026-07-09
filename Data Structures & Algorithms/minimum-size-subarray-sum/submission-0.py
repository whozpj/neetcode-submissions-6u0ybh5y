class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        


        curr = 0
        minLen = float('inf')
        left = 0
        right = 0


        while right <= len(nums)-1:

            curr += nums[right]
            
            if curr >= target:
                #calculate and start reducing
                while curr >= target:
                    minLen = min(minLen, right - left + 1)
                    curr -= nums[left]
                    left += 1
            right += 1

        if minLen == float('inf'):
            return 0
        return minLen
