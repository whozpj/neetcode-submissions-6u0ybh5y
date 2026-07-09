class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #use a set and just add and remove from it
        if k == 0:
            return False

        if len(nums) == 0:
            return False

        seen = set()
        for i in range(0,k+1):
            if i <= len(nums)-1:
                seenLen = len(seen)
                seen.add(nums[i])
                if seenLen == len(seen): #Duplicate here
                    return True

        left = 0
        right = k + 1

        while right <= len(nums)-1:
            
            seen.remove(nums[left])
            seen.add(nums[right])

            if len(seen) != k+1:
                return True

            left += 1
            right += 1

        return False