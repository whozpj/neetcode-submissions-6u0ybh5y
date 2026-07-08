class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        currMax = currMin = nums[0]
        result = max(nums)

        for num in nums[1:]:

            tempMax = max(num, num*currMax, num*currMin)
            currMin = min(num, num*currMax, num*currMin)

            currMax = tempMax

            result = max(currMax, result)
        return result