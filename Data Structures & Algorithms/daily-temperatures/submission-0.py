class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        index = 0
        while index < len(temperatures):
            print (temperatures[index])
            current = temperatures[index]
            if stack and current > temperatures[stack[-1]]:
                popped = stack.pop()
                result[popped] = index - popped
            else:
                stack.append(index)
                index += 1
            print(result)
        return result