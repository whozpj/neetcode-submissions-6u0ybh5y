class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
        start = 0
        end = len(s)-1

        while end>start:
            if s[start] not in letters:
                start += 1
            elif s[end] not in letters:
                end -=1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
        return True