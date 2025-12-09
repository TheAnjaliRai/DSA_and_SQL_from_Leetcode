class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mpp = {}
        zero = 0 
        one = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff = zero - one
            if diff not in mpp and diff != 0:
                mpp[diff] = i
            elif diff in mpp:
                ans = max(ans,i-mpp[diff])
            elif diff == 0:
                ans = max(ans,i+1)
        return ans


        