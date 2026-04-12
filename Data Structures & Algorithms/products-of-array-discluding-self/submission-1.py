class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixArr = []
        postfixArr = []

        # prefix
        prev = 1
        for i in range(len(nums)):
            prefixArr.append(prev)
            prev *= nums[i]

        # postfix
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixArr.insert(0, prev)
            prev *= nums[i]

        # result
        res = []
        for i in range(len(nums)):
            res.append(prefixArr[i] * postfixArr[i])

        return res