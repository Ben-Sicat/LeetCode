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
            currSum += 0
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