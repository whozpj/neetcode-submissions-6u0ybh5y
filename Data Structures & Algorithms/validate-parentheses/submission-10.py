class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 == 1:
            return False

        openingChars = '{(['
        stack = []

        for symbol in s:
            if symbol in openingChars:
                stack.append(symbol)
            elif len(stack)>=1:
                opener = stack.pop()
                if (symbol == ')' and opener != '(') or (symbol == ']' and opener != '[') or (symbol == '}' and opener != '{'):
                    return False
            else: return False
        return len(stack) == 0