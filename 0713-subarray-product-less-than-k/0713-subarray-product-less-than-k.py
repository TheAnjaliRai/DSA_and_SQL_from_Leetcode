class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        cnt = 0 
        prod = 1
        for right in range(0,len(nums)):
            prod *= nums[right]
            while prod >= k and left<=right:
                prod//=nums[left]
                left+=1
            cnt += (right-left+1)
        return cnt

        