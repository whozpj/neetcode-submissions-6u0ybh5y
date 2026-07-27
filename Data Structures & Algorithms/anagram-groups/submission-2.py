class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key is the ord thing list(tuple)


        seen = {}

        for word in strs:

            key = [0]*26

            for letter in word:
                key[ord(letter) - ord('a')] += 1

            key = tuple(key)

            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]


        return list(seen.values())