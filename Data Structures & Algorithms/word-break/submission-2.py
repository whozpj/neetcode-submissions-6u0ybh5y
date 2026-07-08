class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        def dp(index, memo):

            #baseCases:

            if index in memo:
                return memo[index]
            if index == len(s):
                return True
            if index > len(s):
                return False

            for word in wordDict:
                if s[index:].startswith(word):
                    if dp(index+len(word), memo):
                        memo[index] = True
                
            
            if index in memo:
                return memo[index]
            else:
                memo[index] = False
                return False

        return dp(0,{})