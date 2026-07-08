class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.result = 0

        def backtrack(index, currXOR):

            if index == len(nums):
                self.result += currXOR
                return
            
            else:
                backtrack(index+1, currXOR^nums[index])
                backtrack(index+1, currXOR)

        backtrack(0,0)
        return self.result
