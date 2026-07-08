class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(currList, openUsed, closeUsed):

            #base case
            if len(currList) == n*2:
                result.append(currList[:])
                return

            if openUsed < n:
                backtrack(currList + '(', openUsed + 1, closeUsed)
            if closeUsed < n and openUsed > closeUsed:
                backtrack(currList + ')', openUsed, closeUsed + 1)
            

        backtrack('',0,0)
        return result
            
