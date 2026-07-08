class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplied = 1
        result = []
        prefix = []
        suffix = []

        for i in nums:
            prefix.append(int(multiplied * i))
            multiplied = multiplied * i
        
        multiplied = 1
        i = len(nums)-1
        while i >= 0:
            suffix.append(int(multiplied * nums[i]))
            multiplied = multiplied * nums[i]
            i -= 1

        suffix.reverse()

        print(prefix)
        print(suffix)

        for j in range(len(nums)):
            if j == 0:
                result.append(suffix[1])
            elif j == len(nums)-1:
                result.append(prefix[j-1])
            else:
                result.append(prefix[j - 1] * suffix[j+1])
        return result



