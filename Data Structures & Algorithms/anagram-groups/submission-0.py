class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for s in strs:
            sorte = ''.join(sorted(s))
            dict[sorte].append(s)
        return list(dict.values())