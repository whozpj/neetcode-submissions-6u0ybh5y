class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicty = {}
        max_count = 0
        longest = 0
        right = 0
        left = 0
        prevleft = 0

        

        while right < len(s):
            dicty[s[right]] = dicty.get(s[right], 0) + 1
            max_count = max(max_count, dicty[s[right]])

            if (right - left + 1) - max_count > k:
                dicty[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest




        


