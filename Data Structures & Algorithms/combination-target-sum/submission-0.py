class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        result = []

        def backtrack(startIndex, currentList, currentSum):

            if currentSum == target:
                result.append(currentList[:])
                return
            if currentSum > target:
                return
            #we
            for i in range(startIndex,len(nums)):
                backtrack(i, currentList+[nums[i]],currentSum+nums[i])
        
        backtrack(0,[],0)
        return result

            


        '''
        
        base case: if we find the number, then return, or if we go over
    
        
        '''