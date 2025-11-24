class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = 0
        cnt = 0
        prod = 1
        while high < len(nums):
            prod = prod * nums[high]
            while low <= high and prod>=k:
                prod //=nums[low]
                low+=1
            cnt += high-low+1
            high+=1
        return cnt

        