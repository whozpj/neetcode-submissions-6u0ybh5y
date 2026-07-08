class Solution:
    def numDecodings(self, s: str) -> int:
        

        #either you can take one digit or two digits --- if valid, add a plus one, if not, add 0
        #if the start is a zero, then not valid

        validFirsts = ['1','2','3']


        def dp(i, memo):
        #base cases

            if i in memo:
                return memo[i]

            #yay we got to end
            if i == len(s):
                return 1

            #we cant do shit
            if s[i] == '0':
                return 0

            if (i+1 < len(s)) and (10 <= int(s[i:i+2]) <= 26):
                memo[i] = dp(i+1, memo) + dp(i+2, memo)

            else:
                memo[i] = dp(i+1, memo)

            return memo[i]

        return dp(0, {})

