class Solution(object):
    def maxSubArray(self, nums):
        currsum = 0
        maxisum = nums[0]
        for i in range(len(nums)):
            currsum = currsum + nums[i]
            maxisum = max(maxisum , currsum)
            if currsum<0:
                currsum = 0
        return maxisum

        