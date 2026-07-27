class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):

            whatIneed = target - nums[i]

            if whatIneed in seen:
                if seen[whatIneed] > i:
                    return [i, seen[whatIneed]]
                else:
                    return [seen[whatIneed], i]

            seen[nums[i]] = i