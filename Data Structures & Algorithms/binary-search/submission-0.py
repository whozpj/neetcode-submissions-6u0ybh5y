class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        lowerbound = 0
        upperbound = len(nums)-1

        while lowerbound <= upperbound:
            mid = (upperbound+lowerbound)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lowerbound = mid + 1
            elif nums[mid] > target:
                upperbound = mid - 1
        
        return -1