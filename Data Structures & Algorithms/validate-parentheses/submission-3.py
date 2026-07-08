class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2!=0:
            return False
        stack = []
        openingset = set()
        openingset.add('(')
        openingset.add('{')
        openingset.add('[')

        for symbol in s:
            if symbol in openingset:
                stack.append(symbol)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if symbol == ')' and curr != '(':
                    return False
                if symbol == ']' and curr != '[':
                    return False
                if symbol == '}' and curr != '{':
                    return False
        if stack:
            return False
        return True
        