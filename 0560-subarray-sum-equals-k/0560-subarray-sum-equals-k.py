class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mpp = {}
        mpp[0]=1
        sum = 0
        count = 0
        for num in nums:
            sum+=num
            if sum-k in mpp:
                count+= mpp[sum-k]
            mpp[sum] = mpp.get(sum,0)+1
        return count
            



        