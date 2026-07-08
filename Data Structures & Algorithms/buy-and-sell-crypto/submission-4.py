class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0

        head = 1
        tail = 0

        while (head <= len(prices)-1):
            print('comparing, ', prices[head], prices[tail])
            if prices[head]>=prices[tail]:
                mp = max(prices[head]-prices[tail], mp)
            else:
                tail = head
            head += 1

        return mp


            


             