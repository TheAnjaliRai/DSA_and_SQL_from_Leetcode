class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums)-1
        i = 0
        while i<=high:
            if nums[i]==0:
                nums[i],nums[low]=nums[low],nums[i]
                low+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[high],nums[i]=nums[i],nums[high]
                high-=1
        