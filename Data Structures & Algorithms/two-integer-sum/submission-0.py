class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in d:
                return [d[need],i]
            d[nums[i]] = i