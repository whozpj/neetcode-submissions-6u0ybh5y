class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        


        self.result = []

        def backtrack(index, curr):

            if len(curr) == k:
                self.result.append(curr)
                return
            
            if index > n:
                return

            backtrack(index + 1, curr + [index])
            backtrack(index + 1, curr)


        backtrack(1,[])
        return self.result
            

