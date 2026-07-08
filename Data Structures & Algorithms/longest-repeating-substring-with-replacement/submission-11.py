class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        map = {}
        result = 0
        maxFrequency = 0
        right,left = 0,0

        while right<len(s):
            map[s[right]] = 1 + map.get(s[right],0)

            maxFrequency = max(maxFrequency, map[s[right]])

            while (right-left+1) - maxFrequency > k:
                map[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
            right += 1
        return result





