class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        s = []
        s.append(0)
        for i in range(0,len(nums)):
            sum+=nums[i]
            s.append(sum)


        
        for i in range(1,len(s)):
            if s[i-1]==s[len(s)-1]-s[i]:
                return i-1

        
        return -1

        