class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        result = []


        def isPalindrom(s):
            return s == s[::-1]
        def backtrack(startIndex, currList):
            if startIndex == len(s):
                result.append(currList[:])
                return
            
            for endIndex in range(startIndex+1,len(s)+1):
             # we do len(s)+1 to we get slice index of len(s)
                substring = s[startIndex:endIndex]

                if isPalindrom(substring):
                    currList.append(substring)
                    backtrack(endIndex, currList)
                    currList.pop()
        backtrack(0,[])
        return result



                
