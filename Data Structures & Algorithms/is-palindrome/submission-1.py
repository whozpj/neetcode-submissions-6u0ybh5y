class Solution:
    def isPalindrome(self, s: str) -> bool:
        # withoutspaces = ''
        # for letter in s:
        #     if letter != ' ' and (letter.isalpha() or letter.isdigit()):
        #         withoutspaces += (letter.upper())
        # backwards = withoutspaces[::-1]

        # if withoutspaces == backwards:
        #     return True
        # return False

        def isValid(letter):
            if letter.isalpha() or letter.isdigit():
                return True
            return False

        left = 0
        right = len(s)-1
        
        while left<right:
            if isValid(s[left]) and isValid(s[right]):
                if s[left].upper() != s[right].upper():
                    return False
                left += 1
                right -=1
            elif isValid(s[right]) == False:
                right -= 1
            elif isValid(s[left]) == False:
                left += 1
        return True
 