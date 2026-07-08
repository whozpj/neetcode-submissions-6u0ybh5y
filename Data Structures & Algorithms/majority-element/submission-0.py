class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majorityElement = None
        count = 0


        for num in nums:
            if not majorityElement and count == 0:
                majorityElement = num
                count += 1

            else:
                if num == majorityElement:
                    count += 1
                else:
                    count -= 1
                    if count < 0:
                        majorityElement = num
                        count = 1

        return majorityElement