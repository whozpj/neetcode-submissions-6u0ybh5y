class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
         
        result = []
        nums.sort()


        def backtrack(index, currList):
            
            if index == len(nums):
                result.append(currList[:])
                return

            #take

            backtrack(index+1, currList+[nums[index]])

            #dont take

            currentVal = nums[index]

            while index < len(nums) and nums[index] == currentVal:
                index += 1
            
            backtrack(index, currList)
        backtrack(0,[])

        return result