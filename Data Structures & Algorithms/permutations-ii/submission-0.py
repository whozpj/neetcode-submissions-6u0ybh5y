class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        

        #if you dont take it, skip all the way to the end.
        #if you do take it, we can keep
        #keep track of a set of indexes called used to see which we can use and which we cant

        nums.sort()
        self.result = []


        def backtrack(used, curr):

            if len(used) == len(curr) == len(nums):
                self.result.append(curr[:])
                return
            
            i = 0
            while i < len(nums):
                num = nums[i]
                if i in used:
                    i+= 1
                    continue
                else:

                    #take
                    used.add(i)
                    curr.append(num)
                    backtrack(used, curr)
                    used.remove(i)
                    curr.pop()

                    #move onto next
                    while i < len(nums) and nums[i] == num:
                        i += 1
        backtrack(set(), [])
        return self.result
 