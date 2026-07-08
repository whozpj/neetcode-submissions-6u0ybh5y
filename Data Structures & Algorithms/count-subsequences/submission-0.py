class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        def backtrack(indexOfS,indexOfT, memo):

            if (indexOfS,indexOfT) in memo:
                return memo[(indexOfS,indexOfT)]
            
            if indexOfT == len(t):
                return 1
            
            if indexOfS == len(s):
                return 0

            

            if s[indexOfS] == t[indexOfT]:
                memo[(indexOfS,indexOfT)] = backtrack(indexOfS+1, indexOfT+1, memo) + backtrack(indexOfS + 1, indexOfT, memo)
                return memo[(indexOfS,indexOfT)]
            else:
                memo[(indexOfS,indexOfT)] = backtrack(indexOfS + 1, indexOfT, memo)
                return memo[(indexOfS,indexOfT)]

        return backtrack(0,0, {})