class Solution:
    def isHappy(self, n: int) -> bool:
        

        seen = set()

        while True:
            
            s = 0
            for digit in str(n):
                s += int(digit) * int(digit)

            if s == 1:
                return True
            if s in seen:
                return False

            n = s

            seen.add(s)