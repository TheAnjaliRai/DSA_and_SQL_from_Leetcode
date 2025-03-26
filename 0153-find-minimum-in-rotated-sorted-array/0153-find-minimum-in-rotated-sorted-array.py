class Solution(object):
    def findMin(self, nums):
        mini = nums[0]
        for num in nums:
            mini = min(mini,num)
        return mini
        