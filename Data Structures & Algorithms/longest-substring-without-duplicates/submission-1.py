class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        dict = {}
        r = 1
        l = 0
        m = 0
        dict[s[0]] = 1

        while (r < len(s)):
            if dict.get(s[r], 0) == 0:
                dict[s[r]] = 1
                r += 1
                m = max(m, r-l)
            elif dict.get(s[r]) == 1:
                del dict[s[l]]
                l += 1
        return m


