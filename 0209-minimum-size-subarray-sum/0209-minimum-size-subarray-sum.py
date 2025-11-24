class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = 0
        result = len(nums)+1
        sum = 0
        while high < len(nums):
            sum = sum + nums[high]
            while sum>=target:
                result = min(result,(high-low +1))
                sum = sum - nums[low]
                low+=1
            high+=1
        if result == len(nums)+1:
            return 0
        else:
            return result
            