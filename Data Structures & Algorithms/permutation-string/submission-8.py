class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        oneOrd = [0]*26
        twoOrd = [0]*26

        for s in s1:
            oneOrd[ord(s)-ord('a')] += 1

        for s in range(len(s1)):
            twoOrd[ord(s2[s])-ord('a')] += 1

        left = 0
        right = len(s1)-1

        while right<len(s2):
            
            if twoOrd == oneOrd:
                return True
            
            right += 1
            if right<len(s2):
                twoOrd[ord(s2[right])-ord('a')] += 1
            twoOrd[ord(s2[left])-ord('a')] -= 1
            left += 1
        return False



        