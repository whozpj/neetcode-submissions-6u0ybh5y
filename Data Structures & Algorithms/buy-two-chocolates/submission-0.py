class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        result = money


        for i in range(2):
            result -= prices[i]

        if result >= 0:
            return result

        return money
