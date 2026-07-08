class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        numsRemoved = 0

        i = 0
        while i < len(nums):

            if nums[i] == val:
                nums.pop(i)
                nums.append('_')
                numsRemoved += 1
            else:
                i += 1

        return len(nums) - numsRemoved
            