class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0


        for i in range(len(s)):

            result += 1


            curr = s[i]

            if i >= 1 and i < len(s)-1: 
                left = i-1
                right = i+1

                going = True

                while s[left] == s[right] and going:
                    result += 1
                    curr += s[right]
                    curr = s[left] + curr
                    if (left-1) >= 0:
                        left -= 1
                    else: 
                        going = False
                    if (right + 1) < len(s):
                        right += 1
                    else:
                        going = False            

            #Even Case
            curr = ''
            if i >= 1: 
                left = i-1
                right = i

                going = True

                while s[left] == s[right] and going:
                    result += 1
                    curr += s[right]
                    curr = s[left] + curr
                    if (left-1) >= 0:
                        left -= 1
                    else: 
                        going = False
                    if (right + 1) < len(s):
                        right += 1
                    else:
                        going = False
        return result