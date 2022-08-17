class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            l, r = i+1, len(nums)-1

            if i > 0:
                continue
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                
            
            
            
            return res
