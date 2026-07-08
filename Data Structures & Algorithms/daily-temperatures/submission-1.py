class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        
        for n in range(len(temperatures)):

            if len(stack)!=0:
                prevVar, prevIndex = stack[-1]
                curVar = temperatures[n]

                while curVar > prevVar and len(stack)!=0:
                    pv, pi = stack.pop()
                    result[pi] = n-pi
                    if len(stack) != 0:
                        prevVar, prevIndex = stack[-1]

            stack.append((temperatures[n],n))
        return result
        
        #append to the stack:
        #check if the next var is greater
        #if so, then subtract the indexes
        #keep going
 