class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        #append to the stack from the start, a tuple with the temp as well as the index
        # before adding to stack, compare the temps, if the temp is greater, do the index calc and
        #append to the result list



        stack = [ (temperatures[0], 0) ]
        result = []

        for i in range(len(temperatures)):
            result.append(0)


        for i in range(1, len(temperatures)):

            if stack:
                while stack and temperatures[i] > stack[-1][0]:

                    stemp, si = stack.pop()
                    result[si] = i-si
            stack.append((temperatures[i], i))

        return result

            