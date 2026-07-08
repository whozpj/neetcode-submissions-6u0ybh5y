class Solution:
    def isPalindrome(self, s: str) -> bool:
        withoutspaces = ''
        for letter in s:
            if letter != ' ' and (letter.isalpha() or letter.isdigit()):
                withoutspaces += (letter.upper())
        backwards = withoutspaces[::-1]

        if withoutspaces == backwards:
            return True
        return False