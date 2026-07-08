class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        result = ''


        for i in range(len(s)):

            #Odd Case
            curr = s[i]

            if i >= 1 and i < len(s)-1: 
                left = i-1
                right = i+1

                going = True

                while s[left] == s[right] and going:
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


            if len(curr) > len(result):
                result = curr

            

            #Even Case
            curr = ''
            if i >= 1: 
                left = i-1
                right = i

                going = True

                while s[left] == s[right] and going:
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


            if len(curr) > len(result):
                result = curr
        return result



