class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums)-1
        left = 0
        res = nums[0]


        while left <= right:
            #is already sorted, so we know left is smallest
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break

            middle = (left + right)//2
            res = min(res,nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle -1
        return res



