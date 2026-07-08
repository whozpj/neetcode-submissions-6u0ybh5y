class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        map = {}
        maxFrequency = 0
        maxLen = 0

        left,right = 0,0

        while right < len(s):

            map[s[right]] = 1 + map.get(s[right],0)
            
            maxFrequency = max(maxFrequency, map[s[right]])

            if (right-left+1 - maxFrequency) > k:

                map[s[left]] = map[s[left]] - 1
                left += 1
            else:
                maxLen = max(maxLen, right-left + 1)
            right += 1

        return maxLen

    





