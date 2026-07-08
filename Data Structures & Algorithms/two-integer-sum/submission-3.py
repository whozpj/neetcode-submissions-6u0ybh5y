class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [min(seen[need], i),max(seen[need], i)]
            else:
                seen[nums[i]] = i

