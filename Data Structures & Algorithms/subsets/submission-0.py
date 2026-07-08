class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        def backtrack(index, currList):
            #base case - we reached the leaf node, append
            if index == len(nums):
                result.append(currList.copy())
                return            

            #take it:
            backtrack(index+1, currList+[nums[index]])

            #dont take it
            backtrack(index+1, currList)

        backtrack(0,[])
        return result

    '''
so at each level of the decision tree (index), we either
choose to include the number or choose not to. we do this recursively

base case: if index is equal to len(out of bounds), stop, we went through all,
so append the final leaf node
else, we include, so we re-run recurision on array with it included
or we disinclude, re-run recursion on the next index, without including prev


'''

        