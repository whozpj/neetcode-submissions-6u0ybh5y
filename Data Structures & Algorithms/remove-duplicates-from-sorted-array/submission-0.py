class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        placingIndex = 0
        seen = set()



        for num in nums:
            if num not in seen:
                nums[placingIndex] = num
                seen.add(num)
                placingIndex += 1

        return placingIndex