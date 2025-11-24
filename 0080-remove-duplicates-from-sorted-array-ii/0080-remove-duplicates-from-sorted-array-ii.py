class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 2

        for read in range(2,len(nums)):
            if nums[read]!=nums[write-2]:
                nums[write] = nums[read]
                write+=1
        return write


        
        