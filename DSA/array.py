#217 Easy
def containsDuplicate(sef, nums: list[int]) -> bool:
    hash = set()
    for i in nums:
        if i in hash:
            return True
        hash.add(i)
    return False
#53 Medium
def maxSubArray(self,nums: list[int]) -> int:
    maxSub = nums[0] # init variables
    currSum = 0

    for i in nums:
        if currSum < 0: # if current sum is negative, reset it to 0
            currSum = 0
        currSum += i # add current number to current sum
        maxSub = max(maxSub, currSum) #differentiate between what's higher on the max sum and current sum
    return maxSub

# 1 Easy
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # loop through the list and subtract the current number from the target and check if it's in the list / hash
    # if it is, return the index of the current number and the index of the number in the list
    hash = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash:
            return [hash[diff], i]#since were looking for the index of the number in the list, we need to return the index of the number in the list
        hash[nums[i]] = i
#88 Easy
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    last = n + m -1

    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            print("heh")
            n -= 1
        last -= 1
    while n > 0:
        nums1[last] = nums2[n-1]
        n, last  = n-1, last-1
    return nums1
print(merge([0], 0, [1], 1))

def matrixReshape(self, nums: list[list[int]], r: int, c: int) -> list[list[int]]:
    if r * c != len(nums) * len(nums[0]):
        return nums
    new_nums = []
    for i in range(r):
        new_nums.append([])
        for j in range(c):
            new_nums[i].append(nums[i*c+j][j])
    return new_nums

