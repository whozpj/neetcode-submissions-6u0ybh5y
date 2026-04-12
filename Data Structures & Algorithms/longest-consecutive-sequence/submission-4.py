class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for n in nums:
            if n-1 not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longestSequence = max(longestSequence, length)
        return longestSequence