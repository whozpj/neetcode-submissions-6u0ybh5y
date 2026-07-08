class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        upper = max(piles)
        lower = 1
        result = upper

        while upper >= lower:
            middle = (upper + lower)//2
            amtOfTime = 0
            for num in piles:
                amtOfTime += math.ceil(num/middle)

            if amtOfTime <= h:
                result = middle
                upper = middle -1
            elif amtOfTime > h:
                lower = middle + 1

        return result
