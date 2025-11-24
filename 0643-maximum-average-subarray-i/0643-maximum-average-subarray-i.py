class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0.00000
        
        l = 0
        r = k-1
        for i in range(k):
            sum = sum + nums[i]
        max_sum = sum
        while r<len(nums)-1:
            sum = sum - nums[l] + nums[r+1]
            max_sum = max(max_sum,sum)
            l+=1
            r+=1
        return max_sum/k





        