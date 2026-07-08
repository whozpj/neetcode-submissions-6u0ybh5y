class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []
        def backtrack(index, currSum, currList):

            #base cases
            if currSum == target:
                result.append(currList[:])
                return
            if currSum > target:
                return
            if index == len(candidates):
                return

            #take
            backtrack(index+1, currSum + candidates[index], currList + [candidates[index]])

            #dont take
            currentNum = candidates[index]
            while index < len(candidates) and currentNum == candidates[index]:
                index += 1

            backtrack(index, currSum, currList)

        backtrack(0,0,[])
        return result
            