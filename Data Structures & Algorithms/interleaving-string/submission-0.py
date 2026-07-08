class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        #need to keep track of which index we are at in each string
        
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}


        def backtrack(i1, i2, i3):

            if i3 == len(s3):
                if i1 == len(s1) and i2 == len(s2):
                    return True
                else:
                    return False

            if (i1,i2,i3) in memo:
                return memo[(i1,i2,i3)]

            #i1 match:
            i1match = False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                i1match = backtrack(i1+1, i2, i3 + 1)
            
            #i2 match:
            i2match = False
            if i2 < len(s2) and s2[i2] == s3[i3]:
                i2match = backtrack(i1, i2+1, i3 + 1)


            memo[(i1,i2,i3)] = i1match or i2match
            return memo[(i1,i2,i3)]
        return backtrack(0,0,0)