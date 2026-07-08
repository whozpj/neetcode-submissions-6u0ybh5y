class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        if len(s) ==0:
            return 0    
        
        maxSubstring = 1

        left = 0
        right = 0

        seen = set()

        while (right<len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1

            seen.add(s[right])
            maxSubstring = max(maxSubstring,len(seen))
            right +=1
        return maxSubstring