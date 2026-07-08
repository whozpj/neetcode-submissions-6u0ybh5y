class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longestPrefix = ''
        i = 0
        seen = set()
        going = True

        while True:
            for word in strs:
                if i < len(word):
                    seen.add(word[i])
                else:
                    going = False
                    break
            if going and len(seen) == 1:
                longestPrefix = longestPrefix + strs[0][i]
                seen = set()
                i += 1
            else:
                break
        return longestPrefix





                    