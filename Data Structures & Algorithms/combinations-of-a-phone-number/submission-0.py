class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []

        hashmap = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'}


        result = []

        def backtrack(index, currVal):
            
            if index == len(digits):
                result.append(currVal)
                return
            for neighbor in hashmap[int(digits[index])]:
                backtrack(index+1, currVal+neighbor)
        backtrack(0,'')
        return result
