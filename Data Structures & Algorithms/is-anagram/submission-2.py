class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):
            d1 = {}
            d2 = {}

            for i in s:
                if i in d1:
                    d1[i] += 1
                else:
                    d1[i] = 0
            for i in t:
                if i in d2:
                    d2[i] += 1
                else:
                    d2[i] = 0
            return d2 == d1

        return False
            
        
        