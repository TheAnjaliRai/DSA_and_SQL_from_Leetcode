class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        Li= []
        count = 0
        for i in range(0,n):
            if nums[i]!=0:
                Li.append(nums[i])
            else:
                count = count+1
        for i in range(0,count):
            Li.append(0)

        for i in range(n):
            nums[i] = Li[i]