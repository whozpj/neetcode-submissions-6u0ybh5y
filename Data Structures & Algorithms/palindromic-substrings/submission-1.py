class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0


        for i in range(len(s)):

            result += 1

            if i >= 1 and i < len(s)-1: 
                left = i-1
                right = i+1


                while s[left] == s[right]:
                    result += 1
                    
                    if (left-1) >= 0:
                        left -= 1
                    else: 
                        break
                    if (right + 1) < len(s):
                        right += 1
                    else:
                        break            

            #Even Case
            if i >= 1: 
                left = i-1
                right = i

                while s[left] == s[right]:
                    result += 1
                    
                    if (left-1) >= 0:
                        left -= 1
                    else: 
                        break
                    if (right + 1) < len(s):
                        right += 1
                    else:
                        break
        return result