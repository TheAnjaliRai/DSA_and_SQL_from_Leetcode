class Solution(object):
    def maxProduct(self, nums):
        left = 1
        right = 1
        n = len(nums)
        maxprod = float('-inf')
        if n==1:
            return nums[0]
        for i in range(n):
            if left==0:
                left = 1
            if right ==0:
                right = 1
            left*=nums[i]
            right*=nums[n-1-i]
            maxprod = max(maxprod,0,left,right)
        return maxprod
        
        