class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        currentI = None
        for i in range(len(nums)):
            if nums[i] != currentI:

                start = i + 1
                end = len(nums)-1

                while start < end:
                    if nums[start] + nums[end] + nums[i] == 0:
                        res.append([nums[i],nums[start],nums[end]])
                        prevend = nums[end]
                        while nums[end] == prevend and start<end:
                            end -=1
                        prevstart=nums[start]
                        while nums[start] == prevstart and start<end:
                            start +=1
                    elif nums[start] + nums[end] + nums[i] > 0:
                        prevend = nums[end]
                        while nums[end] == prevend and start<end:
                            end -=1
                    elif nums[start] + nums[end] + nums[i] < 0:
                        prevstart=nums[start]
                        while nums[start] == prevstart and start<end:
                            start +=1
            currentI = nums[i]
        return res
                