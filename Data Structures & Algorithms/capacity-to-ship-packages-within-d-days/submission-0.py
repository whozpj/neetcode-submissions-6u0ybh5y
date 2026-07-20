class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        left = max(weights)
        right = sum(weights)

        while left <= right:

            maxCapacity = (left + right)//2

            i = 0
            curr = 0
            used_days = 1
            while i < len(weights):
                if curr + weights[i] > maxCapacity:
                    used_days += 1
                    curr = weights[i]
                else:
                    curr += weights[i]
                i += 1

            if used_days <= days: #too big:
                right = maxCapacity - 1
            else:
                left = maxCapacity + 1

        return left



