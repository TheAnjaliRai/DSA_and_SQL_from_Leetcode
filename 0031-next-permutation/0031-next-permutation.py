class Solution(object):
    def nextPermutation(self, nums):
        pivot  = -1;
        for i in range(len(nums)-2 , -1 , -1):
            if(nums[i]<nums[i+1]):
                pivot = i
                break
        if pivot == -1:
            nums = nums.sort()
            return nums
        
        for i in range(len(nums)-1,pivot,-1):
            if(nums[i]>nums[pivot]):
                nums[i],nums[pivot] = nums[pivot],nums[i]
                break
        
        nums[pivot+1:] = reversed(nums[pivot+1:])
        return nums 
        
                
            

        