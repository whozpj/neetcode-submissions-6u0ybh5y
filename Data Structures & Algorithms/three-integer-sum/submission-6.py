class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i>0 and  nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1

            while right > left:
                if nums[right] + nums[left] + nums[i] == 0:
                    result.append([nums[right],  nums[left], nums[i]])

                    left += 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1


                elif (nums[right] + nums[left] + nums[i]) > 0:
                        right -= 1
                else:
                        left += 1
        return result



