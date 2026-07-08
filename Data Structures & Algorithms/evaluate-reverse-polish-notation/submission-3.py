class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tocken in tokens:
            if tocken in '+-*/':
                second = stack.pop()
                first = stack.pop()
                if tocken == '+':
                    stack.append(int(first) + int(second))
                elif tocken == '-':
                    stack.append(int(first) - int(second))
                elif tocken == '*':
                    stack.append(int(first) * int(second))
                elif tocken == '/':
                    stack.append(int(first) / int(second))
            else:
                stack.append(tocken)
        return int(stack.pop())