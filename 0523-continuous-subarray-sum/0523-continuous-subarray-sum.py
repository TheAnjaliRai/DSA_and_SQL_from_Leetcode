class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        mpp = {}
        mpp[0]=-1 #rem : index
        cnt = 0
        sum = 0
        for i in range(len(nums)):
            num = nums[i]
            sum+=num
            if sum%k in mpp:
                if i-mpp[sum%k] > 1:
                    return True
            else:
                mpp[sum%k] = i
        return False


        