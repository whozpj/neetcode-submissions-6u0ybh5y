class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        putposition = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[putposition] = nums[i]
                putposition += 1

        return(putposition)
