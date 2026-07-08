class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        for i in nums:
            l.append([])
        result = []
        dicty = {}
        for number in nums:
            dicty[number] = dicty.get(number, 0) + 1
        for number in dicty:
            l[dicty.get(number, 0)- 1].append(number)
        for i in range(len(l) - 1, -1, -1):
            if l[i] != []:
                for j in l[i]:
                    result.append(j)
                if len(result) == k:
                    return result