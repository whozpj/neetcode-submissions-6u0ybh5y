class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ''


        #create a dictionary with the characters

        dictionary = {}
        for letter in t:
            dictionary[letter] = 1 + dictionary.get(letter, 0)

        soFar = {} # we use this to see current window status


        formed = 0 # this is to see how many are fully there


        minSub = ''
        lenMinSub = float('inf') #results

        r = 0
        l = 0


        while r < len(s):

            if s[r] in dictionary: #check if r in dict

                soFar[s[r]] = 1+soFar.get(s[r], 0) #update curr counter
                if soFar[s[r]] == dictionary[s[r]]:
                    formed += 1 # one is cleared

            while formed == len(dictionary):#we have a valid, need to figure out shrinking

                if lenMinSub > r-l:
                    minSub = s[l:r+1]
                    lenMinSub = len(minSub) #update result

                if s[l] in dictionary:

                    soFar[s[l]] -= 1

                    if soFar[s[l]] < dictionary[s[l]]:
                        formed -= 1
                     
                l += 1
            
            r += 1 
        return minSub

            
            
            

                

